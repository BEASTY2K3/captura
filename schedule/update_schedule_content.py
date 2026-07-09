filepath = "/Users/harivignesh/Downloads/Photography contest/photography website/ykproduce.co.jp/schedule/index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero Title
content = content.replace("Wedding & Portrait Section", "Event Schedule")
content = content.replace("ウェディング事業", "December 21st, 2026")

# 2. Your Story section
content = content.replace("Your Story,<br />Our Artistry", "Workshops & Agenda")
old_feel_text = """        <p>
          1999年の創業以来、約30万組の結婚式を撮影し、通算60万点を超える写真・映像を制作してきました。<br />
          約400名のクリエイター（フォトグラファー・ビデオグラファー・エディター）が、ウェディングシーンのかけがえのない瞬間をとらえ、未来に残します。
 
        </p>"""

new_feel_text = """        <p>
          Experience a full day of expert-led photography workshops, engaging panel discussions, 
          live practical shooting sessions, and spot-judgement awards. Connect with industry experts 
          and fellow passionate creators.
        </p>"""
content = content.replace(old_feel_text, new_feel_text)

# 3. Photo Section Sticky Title
content = content.replace('<span class="en u-en" data-split-target data-from="#111" data-to="#fff">Wedding & Portrait</span>', '<span class="en u-en" data-split-target data-from="#111" data-to="#fff">Visual Timeline</span>')

# 4. Brand Section -> Event Agenda
content = content.replace('our service brand <span class="small">(Wedding & Portrait Section)</span>', 'Interactive Agenda')
content = content.replace('<img src="../wp-content/themes/ykproduce/assets/images/wedding/k2-logo.svg" alt="K2">', '<div style="font-family:\'Poppins\',sans-serif;font-weight:900;font-size:32px;color:#000;letter-spacing:1px;line-height:1.2;">Frames of India<br><span style="color:#666;font-size:24px;">Agenda 2026</span></div>')

old_k2_box = """      <h2 class="p-wedding-k2__title">
        何気ない瞬間に息づくおふたりらしさを見つけ、<br class="u-pc" />
        芸術的にきりとることを追求する「K2」ブランド
      </h2>
      <p class="p-wedding-k2__text">
        特別な一日に関わる人々の目線や仕草、感情の機微を丁寧にとらえ、<br />
        1カット1カットにその日の空気感や温もりをうつします。<br />
        その連なりは唯一無二の物語を描きだし、かけがえのない一日を美しく彩り<br />
        おふたりの記憶に寄り添いつづけます。
      </p>"""

new_k2_box = """      <h2 class="p-wedding-k2__title">
        December 21st, 2026 — Hindusthan Engineering College Campus
      </h2>
      <div style="margin-top:20px; font-family:\'Poppins\', sans-serif;">
        <table style="width:100%; border-collapse:collapse; text-align:left; color:#333;">
          <tr style="border-bottom:1px solid #ddd;">
            <th style="padding:10px 0; font-weight:700;">Time</th>
            <th style="padding:10px 0; font-weight:700;">Event Detail</th>
          </tr>
          <tr style="border-bottom:1px solid #eee;">
            <td style="padding:10px 0; color:#555; width:120px;">09:30 AM</td>
            <td style="padding:10px 0; font-weight:500;">Inauguration & Grand Exhibition Opening</td>
          </tr>
          <tr style="border-bottom:1px solid #eee;">
            <td style="padding:10px 0; color:#555;">10:30 AM</td>
            <td style="padding:10px 0; font-weight:500;">Jury Interaction & Interview Session (Experiences sharing)</td>
          </tr>
          <tr style="border-bottom:1px solid #eee;">
            <td style="padding:10px 0; color:#555;">11:30 AM</td>
            <td style="padding:10px 0; font-weight:500;">IIP Master Class Workshop: "Modern Framing & Lighting"</td>
          </tr>
          <tr style="border-bottom:1px solid #eee;">
            <td style="padding:10px 0; color:#555;">01:00 PM</td>
            <td style="padding:10px 0; font-weight:500;">Lunch Break & Networking</td>
          </tr>
          <tr style="border-bottom:1px solid #eee;">
            <td style="padding:10px 0; color:#555;">02:00 PM</td>
            <td style="padding:10px 0; font-weight:500;">Live Interactive Model Shooting Session</td>
          </tr>
          <tr style="border-bottom:1px solid #eee;">
            <td style="padding:10px 0; color:#555;">04:00 PM</td>
            <td style="padding:10px 0; font-weight:500;">Jury Spot-Judgement & Finalist Review</td>
          </tr>
          <tr style="border-bottom:1px solid #eee;">
            <td style="padding:10px 0; color:#555;">05:00 PM</td>
            <td style="padding:10px 0; font-weight:500;">Grand Awards Ceremony & Closing Remarks</td>
          </tr>
        </table>
      </div>"""

content = content.replace(old_k2_box, new_k2_box)

# Banner
content = content.replace('Your Story, Our Artistry', 'Join the Exhibition & Master Class')
content = content.replace('ウェディングフォト・ムービーのご紹介、受賞歴などの詳細はこちらからご覧いただけます。', 'Apply for registration to submit entries. Top 100 shortlisted will get free entry to all master classes and workshops.')
content = content.replace('https://k2design.co.jp/', '../registration/index.html')

# News
content = content.replace("Contest News <span class='small'>(Wedding & Portrait Section)</span>", "Contest Highlights")
content = content.replace('ウェディング事業', 'Wedding Category')
content = content.replace('【プレスリリース】2026年度 特別審査員決定のお知らせ', 'Press Release: 2026 Special Jury Panel Announced')
content = content.replace('【特別協賛】ブライダル産業新聞社による「ウェディング写真特別賞」新設決定', 'Special Sponsorship: \'Wedding Photo Special Award\' established by Bridal Industry News')
content = content.replace('【展示会情報】KG+ 2026提挙アワード選抜展「記憶の焦点」開催決定', 'Exhibition Info: Selected Award Exhibition \'Memory Focus\' Announced')
content = content.replace('【メディア掲載】ABEMA特別ドキュメンタリーにて本コンテストが特集されました', 'Media Coverage: Featured in ABEMA Special Documentary')
content = content.replace('【パートナーシップ】AsiaWPA（アジアブライダル写真家協会）との審査提携合意', 'Partnership: Judging collaboration agreement signed with AsiaWPA')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Schedule page content updated successfully.")
