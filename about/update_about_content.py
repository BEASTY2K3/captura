import re

filepath = "/Users/harivignesh/Downloads/Photography contest/photography website/ykproduce.co.jp/about/index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero text
content = content.replace("What&#039;s ykp", "About Frames of India")
content = content.replace("Frames of Indiaについて", "About Frames of India")
content = content.replace("What's YKP", "About")

# 2. Mission text
old_mission = """      <h2 class="p-what-mission__title u-en" data-split-target data-from="#111" data-to="#fff">想いをカタチに。<br />
        カタチに遊びを。</h2>
      <p>
        私たちは、<br />
        お客様一人ひとりの「想い」に寄り添い、<br />
        唯一無二の「カタチ」を届けます。<br />

        そのカタチに、「遊び」を加えることで、<br />
        心に余情を残します。
      </p>"""

new_mission = """      <h2 class="p-what-mission__title u-en" data-split-target data-from="#111" data-to="#fff">Capturing Thoughts.<br />
        Shaping Moments.</h2>
      <p>
        We stand close to the thoughts of each participant,<br />
        delivering unique and creative expressions.<br />
        By adding artistic ingenuity to every frame,<br />
        we leave a lasting impression on every heart.
      </p>"""

content = content.replace(old_mission, new_mission)

# 3. Purpose & Policy
content = content.replace('<h2 class="ja" data-split-target data-from="#fff" data-to="#000">開催趣旨</h2>', '<h2 class="ja" data-split-target data-from="#fff" data-to="#000">Event Purpose</h2>')
content = content.replace('<span class="en u-en">Value</span>コアバリュー', '<span class="en u-en">Value</span>Core Values')
content = content.replace('唯一無二の瞬間をとらえる', 'Capturing the one-and-only moment')
content = content.replace('固定観念を超えた創造性', 'Creativity that breaks standard frames')
content = content.replace('被写体と時代に寄り添うまなざし', 'A gaze aligned with the subject and era')

content = content.replace('<h2 class="ja" data-split-target data-from="#fff" data-to="#000">審査方針</h2>', '<h2 class="ja" data-split-target data-from="#fff" data-to="#000">Judging Policy</h2>')
content = content.replace('<h5>表現と共感</h5>', '<h5>Expression & Resonance</h5>')
content = content.replace('技術的な完成度にとどまらず、見る者の心を揺さぶり、深い感情を呼び起こす表現力と個性を最重視します。', 'Beyond technical execution, we prioritize expressive power and individuality that move viewers and evoke deep emotions.')
content = content.replace('<h5>独自性と視点</h5>', '<h5>Uniqueness & Perspective</h5>')
content = content.replace('被写体に対する独自のまなざしや、既成概念にとらわれない斬新なアプローチ、個人の視点を高く評価します。', 'We highly value a unique gaze upon the subject, fresh approaches that defy conventions, and personal perspectives.')
content = content.replace('<h5>真実性と物語</h5>', '<h5>Authenticity & Narrative</h5>')
content = content.replace('一枚の写真、一作のムービーの背景にあるストーリーや、その瞬間に込められた真摯な想いを尊重します。', 'We respect the narrative behind each photo and video, and the sincere intentions infused into that single moment.')

# 4. Profile Table
content = content.replace('<h2 class="ja" data-split-target data-from="#fff" data-to="#000">コンテスト概要</h2>', '<h2 class="ja" data-split-target data-from="#fff" data-to="#000">Contest Profile</h2>')

# Host
content = content.replace('<th>主催</th>', '<th>Organizers</th>')
content = content.replace('全国フォトコンテスト実行委員会<br />\n                Frames of India Committee', 'Mr.Media & YKR Productions and Events')

# Office Location
content = content.replace('<th>事務局所在地</th>', '<th>Venue & Location</th>')
content = content.replace('〒151-0051 東京都渋谷区千駄ヶ谷2-33-8YKビル4F', 'Hindusthan Engineering College, Coimbatore, Tamil Nadu, India')

# Phone
content = content.replace('<th>電話番号</th>', '<th>Contact Number</th>')
content = content.replace('03-5413-6538（代表）', '+91 422 261 1837')

# Backing / Cooperation
content = content.replace('<th>後援・協力</th>', '<th>Co-organizers & Sponsors</th>')
old_backing = """名古屋後援・協力<br />
                〒450-0003 愛知県名古屋市中村区名駅南1-18-11 コアビル 4F
                <br /><br />
                京都後援・協力/京都スタジオ<br />
                〒604-8216 京都府京都市中京区西洞院通六角下ル池須町419-2
                <br /><br />
                福岡後援・協力<br />
                〒810-0022 福岡県福岡市中央区薬院1丁目14番5号 MG薬院ビル 3F"""
new_backing = "Title Sponsor: IIP (Indian Institute of Photography)<br>Sponsors: Sony India, Sigma India, DJI India"
content = content.replace(old_backing, new_backing)

# Event Year
content = content.replace('<th>開催年度</th>', '<th>Event Date</th>')
content = content.replace('2026年度（第5回アワード開催）', 'December 21st, 2026')

# Prizes
content = content.replace('<th>賞金・副賞</th>', '<th>Prizes & Awards</th>')
content = content.replace('総額200万円（グランプリ 100万円、部門賞、審査員特別賞など）', '1st: Sony M4 Camera | 2nd: Sigma 24-70mm Lens | 3rd: DJI RS4 Mini Gimbal')

# Expected Entries
content = content.replace('<th>応募想定数</th>', '<th>Participants & Entries</th>')
content = content.replace('約12,000点（全国規模）', '1000+ Participants, 4000+ Photo Entries')

# Themes / Categories
content = content.replace('<th>応募部門</th>', '<th>Contest Themes</th>')
old_themes = """・ウェディング写真、映像の企画・撮影・制作・販売<br />
                ・写真、映像コンテンツの企画・制作<br />
                ・テレビコマーシャルの企画・制作<br />
                ・グラフィックデザインの企画・制作<br />
                ・広告の企画・制作<br />
                ・VIDEO、DVD、Blu-ray、CD等の原盤の企画・制作<br />
                ・コンサート、イベントの撮影・収録<br />
                ・音楽ソフト、映像ソフトの企画・制作、及び製造、販売<br />
                ・WEBコンテンツ of 企画・制作<br />
                ・イベントの企画・制作<br />
                ・イベント上映映像の企画・制作<br />
                ・K+(ケープラス)アカデミーの運営<br />
                ・上記内容に付帯する著作権の管理、アーティストのマネージメント"""
old_themes_literal = """・ウェディング写真、映像の企画・撮影・制作・販売<br />
                ・写真、映像コンテンツの企画・制作<br />
                ・テレビコマーシャルの企画・制作<br />
                ・グラフィックデザインの企画・制作<br />
                ・広告の企画・制作<br />
                ・VIDEO、DVD、Blu-ray、CD等の原盤の企画・制作<br />
                ・コンサート、イベントの撮影・収録<br />
                ・音楽ソフト、映像ソフトの企画・制作、及び製造、販売<br />
                ・WEBコンテンツの企画・制作<br />
                ・イベントの企画・制作<br />
                ・イベント上映映像の企画・制作<br />
                ・K+(ケープラス)アカデミーの運営<br />
                ・上記内容に付帯する著作権の管理、アーティストのマネージメント"""
content = content.replace(old_themes_literal, "Portrait, Landscape, Street, Wedding, Wildlife, Drone, Mobile Photography")

# Affiliation
content = content.replace('<th>提携アワード</th>', '<th>Collaborations</th>')
content = content.replace('KG+', 'IIP (Indian Institute of Photography)')

# Access
content = content.replace('コンテスト事務局：<br />\n          〒151-0051　東京都渋谷区千駄ヶ谷2-33-8YKビル4F', 'Event Venue:<br>Hindusthan Engineering College,<br>Othakkalmandapam, Coimbatore, Tamil Nadu 641032')
content = content.replace('Google Mapsでみる', 'View on Google Maps')
content = content.replace('https://maps.app.goo.gl/8Wp5d5CpkMaAi8bQ6', 'https://maps.app.goo.gl/9m2Fv6ePpx9uK4BcA')

# 5. Highlights
content = content.replace('Our Two Sections', 'Contest Highlights')
content = content.replace('Wedding & Portrait Section', 'Jury Interaction & Interview')
content = content.replace('ウェディング事業 <span>[写真撮影 / アルバム制作 / 映像制作]</span>', 'Interactive Talk <span>[Experience Sharing & Panel Discussion]</span>')
content = content.replace('href="../wedding/index.html"', 'href="../jury/index.html"')

content = content.replace('Creative & Art Section', 'Master Class & Live Shoot')
content = content.replace('クリエイション事業 <span>[スタジオ運営 / 映像制作 / イベント企画]</span>', 'Workshop <span>[IIP Master Class & Model Shoot]</span>')
content = content.replace('href="../creation/index.html"', 'href="../schedule/index.html"')

# Video description
content = content.replace('Frames of India Water Collection', 'Frames of India Promo Reel')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("About page content updated successfully.")
