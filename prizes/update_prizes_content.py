filepath = "/Users/harivignesh/Downloads/Photography contest/photography website/ykproduce.co.jp/prizes/index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero Title
content = content.replace("Creative & Art Section", "Prizes & Themes")
content = content.replace("クリエイション事業", "Contest Prizes and 7 Themes")

# 2. Feel section
content = content.replace("Feel The Wonder", "Feel The Glory")
old_feel_text = """        <p>
          クリエイティブの力で世の中に変革をもたらし、想いをカタチに未来をデザイン。<br class="u-pc" />
          独創的な発想で、まだ見ぬ魅力と想像を超える付加価値を創出します。
        </p>"""

new_feel_text = """        <p>
          Showcase your unique perspective and compete for premium equipment.<br class="u-pc" />
          The top 100 shortlisted entries will be featured in the grand Coimbatore Exhibition, 
          with the final winners decided through live spot-judgement by our international jury panel.
        </p>"""
content = content.replace(old_feel_text, new_feel_text)

# 3. Photo Section Sticky Title
content = content.replace('<span class="en u-en" data-split-target data-from="#111" data-to="#fff">Creative & Art</span>', '<span class="en u-en" data-split-target data-from="#111" data-to="#fff">Inspiring Frames</span>')
content = content.replace('<span class="ja" data-split-target data-from="#111" data-to="#fff">クリエイション事業</span>', '<span class="ja" data-split-target data-from="#111" data-to="#fff">Captured Moments</span>')

# 4. Brand Section
content = content.replace('our service brand <span class="small">(Creative & Art Section)</span>', 'Contest Prizes & themes')
content = content.replace('<img src="../wp-content/themes/ykproduce/assets/images/creation/kyoto-logo.svg" alt="京都創造ガレージのロゴ">', '<div style="font-family:\'Poppins\',sans-serif;font-weight:900;font-size:32px;color:#000;letter-spacing:1px;line-height:1.2;">Frames of India<br><span style="color:#666;font-size:24px;">Prizes 2026</span></div>')

old_kyoto_box = """      <h2 class="p-creation-kyoto__title">
        新しいクリエイティブを創造し、発信する空間、<br class="u-pc" />
        「京都創造ガレージ」
      </h2>
      <p class="p-creation-kyoto__text">
        ただの箱ではなくコミュニティへ。次世代を創造する新進気鋭の表現者たちが集う空間。<br />
        新しい表現、斬新な演出、ジャンルを超えたコラボレーション。街並みから振る舞いまで、<br />
        これまでの文化が色濃く残る京都という街で、新しい時代の文化をこの場所から。
      </p>
      <h2 class="p-creation-kyoto__title p-creation-kyoto__title--small">
        伝統文化 × クリエイション
      </h2>
      <p class="p-creation-kyoto__text">
        想像から創造へ。京都創造ガレージはこれからの日本文化を創造する発信地になります。
      </p>"""

new_kyoto_box = """      <h2 class="p-creation-kyoto__title">
        Prestige Awards & Premium Photography Equipment<br class="u-pc" />
        "Grand Prizes"
      </h2>
      <p class="p-creation-kyoto__text">
        <strong>1st Prize:</strong> Sony M4 Camera (Body Only) - The ultimate tool for capturing life's defining moments.<br />
        <strong>2nd Prize:</strong> Sigma 24-70mm DG DN II Lens - Perfect sharpness and versatile zoom for all genres.<br />
        <strong>3rd Prize:</strong> DJI RS4 Mini Gimbal - Smooth, cinematic stability for modern visual creators.
      </p>
      <h2 class="p-creation-kyoto__title p-creation-kyoto__title--small">
        7 Contest Themes
      </h2>
      <p class="p-creation-kyoto__text">
        Portrait, Landscape, Street, Wedding, Wildlife, Drone, and Mobile Photography. Submit your work in your preferred theme.
      </p>"""

content = content.replace(old_kyoto_box, new_kyoto_box)

# Banner
content = content.replace('Creative Evolution 創造が未来を変える', 'Submit Your Entry Now')
content = content.replace('スタジオ、レンタルスペース、映像企画・制作、イベント企画・運営、キャスティング、機材レンタルなど、お客様のご要望に応じてご対応致します。', 'Select your category, register details, upload your best captures, and get shortlisted for the Hindusthan College exhibition.')
content = content.replace('https://kyoto-creative-garage.studio/', '../registration/index.html')

# Info items
old_more_item = """    <div class="p-creation-kyoto__more-item">
      <p class="p-creation-kyoto__more-item-title u-en">Access</p>
      <p class="p-creation-kyoto__more-item-text">
        〒604-8216　京都府京都市中京区西洞院通六角下ル池須町419-2西洞院YKビル<br />
        阪急京都線：烏丸駅から徒歩7分 ／ 地下鉄烏丸線：四条駅から徒歩7分<br />
        ※24番出⼝を右⽅向にお進みください
      </p>
      <a href="https://maps.app.goo.gl/vtWtnXzNvXucTmWk6?g_st=com.google.maps.preview.copy" class="p-creation-kyoto__more-map" target="_blank" data-etc-hover>
        <span data-etc-hover-target>Google Mapsでみる</span>
        <svg width="14" height="13" viewBox="0 0 14 13" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M3.47705 3.18213H9.84101L9.84101 9.54609" stroke="black" />
          <line x1="9.35355" y1="3.6265" x2="0.353553" y2="12.6265" stroke="black" />
        </svg>
      </a>
    </div>"""

new_more_item = """    <div class="p-creation-kyoto__more-item">
      <p class="p-creation-kyoto__more-item-title u-en">Shortlist Info</p>
      <p class="p-creation-kyoto__more-item-text">
        Top 100 shortlisted participants will get access tickets for the Coimbatore main event and a spot in the physical gallery exhibition at Hindusthan Engineering College.<br />
        Winner will be declared live during spot-judgement by the jury on Dec 21st, 2026.
      </p>
    </div>"""
content = content.replace(old_more_item, new_more_item)

# Inquiry block
content = content.replace('ご予約やご相談など、お気軽にお問い合わせください。', 'For sponsorship, stalls, or general queries, please reach out to us.')
content = content.replace('075-254-7229', '+91 422 261 1837')
content = content.replace('10:00 〜 19:00', 'Mon - Sat: 9:00 AM - 5:00 PM')
content = content.replace('https://kyoto-creative-garage.studio/contact/', '../contact/index.html')

# News Title
content = content.replace("Contest News <span class='small'>(Creative & Art Section)</span>", "Contest Highlights")

# SNS handles
content = content.replace('@kyogare', '@framesofindia')
content = content.replace('@kyoto_cr_garage', '@framesofindia')
content = content.replace('@kyoto.cr.garage', '@framesofindia')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Prizes page content updated successfully.")
