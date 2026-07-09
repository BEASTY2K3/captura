// CAPTURA Firebase & Razorpay Database Bridge Layer
(function() {
  // Inject Firebase and Razorpay SDK scripts dynamically
  const scriptsToLoad = [
    "https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js",
    "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth-compat.js",
    "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore-compat.js",
    "https://www.gstatic.com/firebasejs/10.8.0/firebase-storage-compat.js",
    "https://checkout.razorpay.com/v1/checkout.js"
  ];

  let loadedCount = 0;
  scriptsToLoad.forEach(url => {
    if (document.querySelector(`script[src="${url}"]`)) {
      loadedCount++;
      if (loadedCount === scriptsToLoad.length) {
        initFirebase();
      }
      return;
    }
    const script = document.createElement('script');
    script.src = url;
    script.async = true;
    script.onload = () => {
      loadedCount++;
      if (loadedCount === scriptsToLoad.length) {
        initFirebase();
      }
    };
    script.onerror = (err) => console.error("Error loading script:", url, err);
    document.head.appendChild(script);
  });

  // Seeds data
  const seedJury = [
    {
      id: "jury_1",
      name: "Andreas Schmidt",
      location: "Berlin, Germany",
      specialty: "Chiaroscuro & Fine Art Photography",
      bio: "A contemporary fine art photographer with over 20 years of experience based in Europe. Renowned for conceptual portraiture leveraging strong contrasts of light and shadow. Exhibited widely in major art institutions including Berlin National Gallery.",
      image: "wp-content/uploads/2026/03/Ando_010.png"
    },
    {
      id: "jury_2",
      name: "Kenji Suzuki",
      location: "Tokyo, Japan",
      specialty: "Documentary & Emotional Portraiture",
      bio: "A leading wedding and portrait photographer in Asia. Spanning commercial shoots to intimate snapshots, he excels in capturing raw emotional moments that tell cohesive stories. Regular jury member for major Asian photo societies.",
      image: "wp-content/uploads/2026/06/2025COSMOSprint_KOSAKA_RYUTO-1024x683.jpg"
    },
    {
      id: "jury_3",
      name: "Emily Laurent",
      location: "Paris, France",
      specialty: "Fashion & Creative Digital Art",
      bio: "Fashion photographer and digital artist based in Paris. Lead visual producer for global high-fashion campaigns, specializing in creative color grading, composite imagery, and advanced post-production styling.",
      image: "wp-content/uploads/2026/06/2025COSMOSprint_NISHIMURA_YUKINA-683x1024.jpg"
    }
  ];

  const seedSubmissions = [
    {
      id: "seed_1",
      userId: "seed_chloe@email.com",
      userName: "Chloe Dubois",
      userSocial: "https://instagram.com/chloe_dubois",
      userBio: "Landscape photographer capturing fog, clouds, and golden peaks.",
      title: "Silent Morning",
      division: "Landscape",
      description: "Captured at dawn in the Himalayas. The morning light hitting the morning fog creates a serene landscape.",
      image: "wp-content/themes/captura/assets/images/home/scene01.jpg",
      likes: 28,
      likedBy: [],
      comments: [
        { name: "Andreas Schmidt", text: "Stunning light control and composition! Perfect showcase of depth.", date: new Date(Date.now() - 3600000 * 24 * 3).toISOString() },
        { name: "Rohan", text: "Absolutely breathtaking! The fog makes it look magical.", date: new Date(Date.now() - 3600000 * 12).toISOString() }
      ],
      date: new Date(Date.now() - 3600000 * 24 * 5).toISOString()
    },
    {
      id: "seed_2",
      userId: "seed_satoshi@email.com",
      userName: "Satoshi Tanaka",
      userSocial: "https://x.com/satoshi_photo",
      userBio: "Wedding & documentary photographer detailing genuine human interactions.",
      title: "Golden Hour Glow",
      division: "Portrait",
      description: "Backlit portrait highlighting the details of the lace veil in the warm setting sun.",
      image: "wp-content/themes/captura/assets/images/wedding/photo-image06.webp",
      likes: 74,
      likedBy: [],
      comments: [
        { name: "Kenji Suzuki", text: "Superb backlight! The details are captured beautifully.", date: new Date(Date.now() - 3600000 * 24 * 2).toISOString() }
      ],
      date: new Date(Date.now() - 3600000 * 24 * 4).toISOString()
    },
    {
      id: "seed_3",
      userId: "seed_arjun@email.com",
      userName: "Arjun Sen",
      userSocial: "https://instagram.com/arjun_clicks",
      userBio: "Street and documentary photographer capturing urban stories.",
      title: "Steps of History",
      division: "Street",
      description: "An elderly craftsman working on his traditional wooden crafts in Varanasi, representing decades of dedication.",
      image: "wp-content/themes/captura/assets/images/home/scene05.jpg",
      likes: 19,
      likedBy: [],
      comments: [
        { name: "Aria", text: "The hands tell such a deep story. Wonderful capture.", date: new Date(Date.now() - 3600000 * 2).toISOString() }
      ],
      date: new Date(Date.now() - 3600000 * 24 * 2).toISOString()
    }
  ];

  const seedSponsors = [
    { id: "sp_1", name: "IIP", image: "wp-content/themes/captura/assets/images/sponsors/iip.svg", link: "https://www.iipedu.com/" },
    { id: "sp_2", name: "Sony", image: "wp-content/themes/captura/assets/images/sponsors/sony.svg", link: "https://www.sony.com/" },
    { id: "sp_3", name: "Canon", image: "wp-content/themes/captura/assets/images/sponsors/canon.svg", link: "https://www.canon.com/" },
    { id: "sp_4", name: "Adobe", image: "wp-content/themes/captura/assets/images/sponsors/adobe.svg", link: "https://www.adobe.com/" },
    { id: "sp_5", name: "SanDisk", image: "wp-content/themes/captura/assets/images/sponsors/sandisk.svg", link: "https://www.sandisk.com/" },
    { id: "sp_6", name: "Mr.Media", image: "wp-content/themes/captura/assets/images/sponsors/mr_media.svg", link: "https://mr-media.in/" }
  ];

  const defaultPricing = {
    "Landscape": 999,
    "Portrait": 999,
    "Street": 999,
    "Wedding": 999,
    "Wild Life": 999,
    "Drone Photography": 999,
    "Mobile Photography": 999
  };

  // Base64 helper
  function base64ToBlob(base64Data, contentType = '') {
    const parts = base64Data.split(';base64,');
    const rawBase64 = parts.length > 1 ? parts[1] : parts[0];
    const detectedType = parts.length > 1 ? parts[0].split(':')[1] : contentType;
    
    const byteCharacters = atob(rawBase64);
    const sliceSize = 1024;
    const byteArrays = [];
    
    for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
      const slice = byteCharacters.slice(offset, offset + sliceSize);
      const byteNumbers = new Array(slice.length);
      for (let i = 0; i < slice.length; i++) {
        byteNumbers[i] = slice.charCodeAt(i);
      }
      const byteArray = new Uint8Array(byteNumbers);
      byteArrays.push(byteArray);
    }
    
    return new Blob(byteArrays, { type: detectedType });
  }

  // Upload helper
  function uploadImageToStorage(base64Data, path) {
    return new Promise((resolve) => {
      if (!base64Data || !base64Data.startsWith('data:image')) {
        // If not a base64 string, just return it
        resolve(base64Data);
        return;
      }
      try {
        const blob = base64ToBlob(base64Data);
        const storageRef = firebase.storage().ref().child(path);
        const uploadTask = storageRef.put(blob);
        
        uploadTask.on('state_changed', 
          null, 
          (error) => {
            console.error("Storage upload error:", error);
            resolve(base64Data); // Fallback
          }, 
          () => {
            uploadTask.snapshot.ref.getDownloadURL().then((downloadURL) => {
              resolve(downloadURL);
            }).catch(() => resolve(base64Data));
          }
        );
      } catch(e) {
        console.error("Blob conversion error:", e);
        resolve(base64Data);
      }
    });
  }

  // Database bridge object
  window.CapturaDB = {
    isSynced: false,
    
    getLocalStorage: function(key, defaultVal) {
      const val = localStorage.getItem(key);
      return val ? JSON.parse(val) : defaultVal;
    },

    setLocalStorage: function(key, val) {
      localStorage.setItem(key, JSON.stringify(val));
    },

    getJury: function() {
      return this.getLocalStorage('npa_jury', seedJury);
    },

    saveJury: async function(juryList) {
      this.setLocalStorage('npa_jury', juryList);
      if (!this.isSynced) return;

      try {
        // Find if there is a new base64 image in the list
        for (let i = 0; i < juryList.length; i++) {
          const item = juryList[i];
          if (item.image && item.image.startsWith('data:image')) {
            const url = await uploadImageToStorage(item.image, `jury/${item.id}`);
            item.image = url;
            juryList[i] = item;
            this.setLocalStorage('npa_jury', juryList);
          }
          // Write to firestore doc
          await firebase.firestore().collection('jury').doc(item.id).set(item);
        }
      } catch (err) {
        console.error("Error writing jury to Firestore:", err);
      }
    },

    getSubmissions: function() {
      return this.getLocalStorage('npa_submissions', seedSubmissions);
    },

    saveSubmissions: async function(subs) {
      this.setLocalStorage('npa_submissions', subs);
      if (!this.isSynced) return;

      try {
        // Upload new base64 images
        for (let i = 0; i < subs.length; i++) {
          const item = subs[i];
          if (item.image && item.image.startsWith('data:image')) {
            const url = await uploadImageToStorage(item.image, `submissions/${item.id}`);
            item.image = url;
            subs[i] = item;
            this.setLocalStorage('npa_submissions', subs);
          }
          await firebase.firestore().collection('submissions').doc(item.id).set(item);
        }
      } catch (err) {
        console.error("Error writing submissions to Firestore:", err);
      }
    },

    getUsers: function() {
      return this.getLocalStorage('npa_users', []);
    },

    saveUsers: async function(users) {
      this.setLocalStorage('npa_users', users);
      if (!this.isSynced) return;

      try {
        for (let user of users) {
          await firebase.firestore().collection('users').doc(user.email).set(user);
        }
      } catch (err) {
        console.error("Error writing users to Firestore:", err);
      }
    },

    deleteUser: async function(email) {
      if (!this.isSynced) return;
      try {
        const db = firebase.firestore();
        
        // 1. Delete user doc
        await db.collection('users').doc(email).delete();
        
        // 2. Delete all user submissions
        const subsSnap = await db.collection('submissions').where('userId', '==', email).get();
        const batch = db.batch();
        subsSnap.docs.forEach(doc => {
          batch.delete(doc.ref);
        });
        await batch.commit();

        // 3. Update local caches
        const users = this.getUsers().filter(u => u.email !== email);
        this.setLocalStorage('npa_users', users);
        
        const subs = this.getSubmissions().filter(s => s.userId !== email);
        this.setLocalStorage('npa_submissions', subs);

        window.dispatchEvent(new CustomEvent('captura-db-synced'));
      } catch (err) {
        console.error("Error deleting user from Firestore:", err);
      }
    },

    deleteSubmission: async function(subId) {
      if (!this.isSynced) return;
      try {
        const db = firebase.firestore();
        
        // 1. Fetch submission details
        const subDoc = await db.collection('submissions').doc(subId).get();
        if (subDoc.exists) {
          const subData = subDoc.data();
          const userId = subData.userId;
          const slotNum = subData.slotNum;
          
          // 2. Fetch owner user and update slot state
          const userDocSnap = await db.collection('users').doc(userId).get();
          if (userDocSnap.exists) {
            const userData = userDocSnap.data();
            userData.slotsUsed = Math.max(0, (userData.slotsUsed || 0) - 1);
            if (userData.purchasedSlots) {
              const slot = userData.purchasedSlots.find(s => s.id === slotNum);
              if (slot) {
                slot.used = false;
              }
            }
            await db.collection('users').doc(userId).set(userData);
          }
        }
        
        // 3. Delete submission document
        await db.collection('submissions').doc(subId).delete();

        // 4. Update local caches
        const subs = this.getSubmissions().filter(s => s.id !== subId);
        this.setLocalStorage('npa_submissions', subs);
        
        // Refresh users list in local cache
        const usersSnap = await db.collection('users').get();
        let usersList = [];
        usersSnap.forEach(doc => usersList.push(doc.data()));
        this.setLocalStorage('npa_users', usersList);

        window.dispatchEvent(new CustomEvent('captura-db-synced'));
      } catch (err) {
        console.error("Error deleting submission from Firestore:", err);
      }
    },

    resetSubmissions: async function() {
      if (!this.isSynced) return;
      try {
        const db = firebase.firestore();
        const snapshot = await db.collection('submissions').get();
        const batch = db.batch();
        snapshot.docs.forEach(doc => batch.delete(doc.ref));
        await batch.commit();

        // Reset user slots used counts
        const usersSnap = await db.collection('users').get();
        for (let userDoc of usersSnap.docs) {
          const userData = userDoc.data();
          userData.slotsUsed = 0;
          if (userData.purchasedSlots) {
            userData.purchasedSlots.forEach(s => s.used = false);
          }
          await db.collection('users').doc(userData.email).set(userData);
        }

        // Update local caches
        this.setLocalStorage('npa_submissions', []);
        
        // Refresh users cache
        const usersSnap2 = await db.collection('users').get();
        let usersList = [];
        usersSnap2.forEach(doc => usersList.push(doc.data()));
        this.setLocalStorage('npa_users', usersList);

        window.dispatchEvent(new CustomEvent('captura-db-synced'));
      } catch (err) {
        console.error("Error resetting submissions collection:", err);
      }
    },

    resetUsers: async function() {
      if (!this.isSynced) return;
      try {
        const db = firebase.firestore();
        
        // 1. Delete all users in Firestore
        const usersSnap = await db.collection('users').get();
        const batch = db.batch();
        usersSnap.docs.forEach(doc => batch.delete(doc.ref));
        await batch.commit();

        // 2. Delete all submissions as well (since they belong to users)
        const subsSnap = await db.collection('submissions').get();
        const batch2 = db.batch();
        subsSnap.docs.forEach(doc => batch2.delete(doc.ref));
        await batch2.commit();

        // Update local caches
        this.setLocalStorage('npa_users', []);
        this.setLocalStorage('npa_submissions', []);

        window.dispatchEvent(new CustomEvent('captura-db-synced'));
      } catch (err) {
        console.error("Error resetting users collection:", err);
      }
    },

    getCurrentUser: function() {
      return this.getLocalStorage('npa_current_user', null);
    },

    setCurrentUser: function(user) {
      this.setLocalStorage('npa_current_user', user);
      if (this.isSynced && user) {
        firebase.firestore().collection('users').doc(user.email).set(user)
          .catch(e => console.error("Error saving current user:", e));
      }
    },

    logout: function() {
      localStorage.removeItem('npa_current_user');
      if (this.isSynced) {
        firebase.auth().signOut().catch(e => console.error("Signout error:", e));
      }
    },

    // Dynamic Sponsors management
    getSponsors: function() {
      return this.getLocalStorage('npa_sponsors', seedSponsors);
    },

    saveSponsors: async function(sponsors) {
      this.setLocalStorage('npa_sponsors', sponsors);
      if (!this.isSynced) return;

      try {
        // First delete all sponsors in Firestore to update collection
        const snapshot = await firebase.firestore().collection('sponsors').get();
        const batch = firebase.firestore().batch();
        snapshot.docs.forEach(doc => batch.delete(doc.ref));
        await batch.commit();

        // Write new ones
        for (let sp of sponsors) {
          if (sp.image && sp.image.startsWith('data:image')) {
            const url = await uploadImageToStorage(sp.image, `sponsors/${sp.id}`);
            sp.image = url;
          }
          await firebase.firestore().collection('sponsors').doc(sp.id).set(sp);
        }
        this.setLocalStorage('npa_sponsors', sponsors);
      } catch (err) {
        console.error("Error writing sponsors to Firestore:", err);
      }
    },

    // Dynamic Category Pricing management
    getPricing: function() {
      return this.getLocalStorage('npa_pricing', defaultPricing);
    },

    savePricing: async function(pricing) {
      this.setLocalStorage('npa_pricing', pricing);
      if (!this.isSynced) return;

      try {
        await firebase.firestore().collection('config').doc('pricing').set(pricing);
      } catch (err) {
        console.error("Error saving pricing to Firestore:", err);
      }
    },

    // Initiate Razorpay Standard Checkout
    initiatePayment: function(email, category, amount, callback) {
      if (typeof Razorpay === 'undefined') {
        alert("Payment gateway loading. Please try again in a few seconds.");
        return;
      }
      
      const options = {
        key: "rzp_test_eU9vV4Wj62mZlW",
        amount: amount * 100, // in paise
        currency: "INR",
        name: "CAPTURA Contest",
        description: `Upload Slot: ${category}`,
        handler: function(response) {
          if (response.razorpay_payment_id) {
            callback(null, response.razorpay_payment_id);
          } else {
            callback(new Error("Razorpay Payment ID missing"));
          }
        },
        prefill: {
          email: email
        },
        theme: {
          color: "#000000"
        }
      };
      
      const rzp = new Razorpay(options);
      rzp.open();
    }
  };

  // Firebase initialization and SWR syncing
  async function initFirebase() {
    const firebaseConfig = {
      apiKey: "AIzaSyCFgsf9gIEt-nUzaN-vknrBef1SvEMCnSk",
      authDomain: "captura-55993.firebaseapp.com",
      projectId: "captura-55993",
      storageBucket: "captura-55993.firebasestorage.app",
      messagingSenderId: "724358290926",
      appId: "1:724358290926:web:1974371a9ebcd045a582ff",
      measurementId: "G-PQFRHJJGRG"
    };

    try {
      if (!firebase.apps.length) {
        firebase.initializeApp(firebaseConfig);
      }
      
      const db = firebase.firestore();
      window.CapturaDB.isSynced = true;
      console.log("Firebase initialized and bridged successfully.");

      // 1. Sync Pricing
      const pricingDoc = await db.collection('config').doc('pricing').get();
      let pricing = defaultPricing;
      if (pricingDoc.exists) {
        pricing = pricingDoc.data();
      } else {
        await db.collection('config').doc('pricing').set(defaultPricing);
      }
      window.CapturaDB.setLocalStorage('npa_pricing', pricing);

      // 2. Sync Sponsors
      const sponsorsSnap = await db.collection('sponsors').get();
      let sponsors = [];
      if (!sponsorsSnap.empty) {
        sponsorsSnap.forEach(doc => sponsors.push(doc.data()));
      } else {
        // Seed default sponsors
        sponsors = seedSponsors;
        for (let sp of seedSponsors) {
          await db.collection('sponsors').doc(sp.id).set(sp);
        }
      }
      window.CapturaDB.setLocalStorage('npa_sponsors', sponsors);

      // 3. Sync Jury
      const jurySnap = await db.collection('jury').get();
      let jury = [];
      if (!jurySnap.empty) {
        jurySnap.forEach(doc => jury.push(doc.data()));
      } else {
        jury = seedJury;
        for (let member of seedJury) {
          await db.collection('jury').doc(member.id).set(member);
        }
      }
      window.CapturaDB.setLocalStorage('npa_jury', jury);

      // 4. Sync Submissions
      const subsSnap = await db.collection('submissions').get();
      let subs = [];
      if (!subsSnap.empty) {
        subsSnap.forEach(doc => subs.push(doc.data()));
      } else {
        subs = seedSubmissions;
        for (let sub of seedSubmissions) {
          await db.collection('submissions').doc(sub.id).set(sub);
        }
      }
      // Sort submissions by date descending
      subs.sort((a, b) => new Date(b.date) - new Date(a.date));
      window.CapturaDB.setLocalStorage('npa_submissions', subs);

      // 5. Sync Users
      const usersSnap = await db.collection('users').get();
      let users = [];
      usersSnap.forEach(doc => users.push(doc.data()));
      window.CapturaDB.setLocalStorage('npa_users', users);

      // 6. Sync Current Logged-in User via Auth Observer
      firebase.auth().onAuthStateChanged(async (authUser) => {
        if (authUser) {
          try {
            const userDocSnap = await db.collection('users').doc(authUser.email).get();
            let userDoc;
            if (userDocSnap.exists) {
              userDoc = userDocSnap.data();
            } else {
              // Sign-in via Google (new user)
              userDoc = {
                name: authUser.displayName || authUser.email.split('@')[0],
                email: authUser.email,
                social: '',
                bio: '',
                purchasedSlots: [],
                slotsPurchased: 0,
                slotsUsed: 0
              };
              await db.collection('users').doc(authUser.email).set(userDoc);
              
              // Refresh user list in local cache
              const usersSnap2 = await db.collection('users').get();
              let usersList = [];
              usersSnap2.forEach(doc => usersList.push(doc.data()));
              window.CapturaDB.setLocalStorage('npa_users', usersList);
            }
            window.CapturaDB.setLocalStorage('npa_current_user', userDoc);
          } catch(e) {
            console.error("Auth user sync failed:", e);
          }
        } else {
          localStorage.removeItem('npa_current_user');
        }
        window.dispatchEvent(new CustomEvent('captura-db-synced'));
      });
      console.log("Firebase sync completed successfully!");

    } catch (err) {
      console.error("Firebase synchronization failed. Working in cache mode.", err);
    }
  }
})();
