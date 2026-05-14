#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1) Update timeline track dots (5 -> 7)
old_dots = '''          <div class="track-dot active" data-day="1">Day 1<br><small>认知<br>入门</small></div>
          <div class="track-dot" data-day="2">Day 2<br><small>情绪<br>流程</small></div>
          <div class="track-dot" data-day="3">Day 3<br><small>客户<br>话术</small></div>
          <div class="track-dot" data-day="4">Day 4<br><small>保护<br>协作</small></div>
          <div class="track-dot" data-day="5">Day 5<br><small>考核<br>上岗</small></div>'''

new_dots = '''          <div class="track-dot active" data-day="1">Day 1<br><small>认知<br>入门</small></div>
          <div class="track-dot" data-day="2">Day 2<br><small>情绪<br>流程</small></div>
          <div class="track-dot" data-day="3">Day 3<br><small>客户<br>话术</small></div>
          <div class="track-dot" data-day="4">Day 4<br><small>保护<br>协作</small></div>
          <div class="track-dot" data-day="5">Day 5<br><small>考核<br>上岗</small></div>
          <div class="track-dot" data-day="6">Day 6<br><small>产品<br>知识</small></div>
          <div class="track-dot" data-day="7">Day 7<br><small>最终<br>考核</small></div>'''

html = html.replace(old_dots, new_dots, 1)

# 2) Update header text
html = html.replace('5天系统学习，从入门到独立上岗', '7天系统学习，从入门到独立上岗', 1)

# 3) Product training content
product_training = '''
  <div class="train-card" id="train11">
    <div class="train-card-header">
      <div class="train-icon">&#x1F9F0;</div>
      <div class="train-meta">
        <div class="train-day">第6天</div>
        <div class="train-title">产品知识培训</div>
        <div class="train-subtitle">熟悉每个品牌的产品线，才能给出专业建议</div>
      </div>
    </div>
    <div class="train-items">
      <div class="train-item">
        <div class="train-label">培训启动</div>
        <div class="train-text">上午：品牌方产品负责人进行2小时产品宣讲（产品成分/功效/适用肤质/使用方法）<br>下午：团队内部学习产品手册，阅读产品评论区常见问题<br>晚上：背诵产品卖点关键词（每个产品3-5个核心卖点）</div>
      </div>
      <div class="train-item">
        <div class="train-label">产品分类框架</div>
        <div class="train-text">精华类：高活性成分（如VC/玻尿酸/烟酰胺），需说明搭配顺序<br>面霜/乳液类：保湿锁水，区分干皮/油皮适用款<br>防晒类：SPF/PA值解读，涂抹量/补涂频率，敏感肌专用款<br>清洁类：卸妆/洁面，皂基vs氨基酸表活，敏感肌/油皮/干皮区分<br>面膜类：贴片vs涂抹，功效区分（补水/美白/舒缓），使用频率建议</div>
      </div>
      <div class="train-item">
        <div class="train-label">成分功效速查表</div>
        <div class="train-text">烟酰胺 → 美白提亮，适合熬夜党<br>玻尿酸 → 深层补水，干燥肌必备<br>VC（抗坏血酸）→ 抗氧化提亮，避光保存<br>视黄醇（A醇）→ 抗老淡纹，孕妇禁用，需建立耐受<br>水杨酸 → 疏通毛孔，油痘肌适用，敏感肌慎用<br>神经酰胺 → 修复屏障，敏感肌/烂脸期可用</div>
      </div>
      <div class="train-item">
        <div class="train-label">常见粉丝问题应答</div>
        <div class="train-text">Q：这个产品适合我吗？ → 询问肤质（干/油/混）+ 当前皮肤状态 + 诉求（美白/抗老/保湿）<br>Q：产品能和其他品牌混用吗？ → 同品类不叠加，不同品类按「清洁→水→精华→乳→霜→防晒」顺序<br>Q：用了过敏怎么办？ → 立即停用，提供购买凭证和就医建议，引导走售后流程</div>
      </div>
    </div>
  </div>
  <div class="train-card" id="train12">
    <div class="train-card-header">
      <div class="train-icon">&#x1F3AF;</div>
      <div class="train-meta">
        <div class="train-day">第7天</div>
        <div class="train-title">最终考核与综合上岗评估</div>
        <div class="train-subtitle">通过全部考核，正式成为团队一员</div>
      </div>
    </div>
    <div class="train-items">
      <div class="train-item">
        <div class="train-label">考核安排</div>
        <div class="train-text">上午笔试（产品知识+服务规范，60分及格）<br>下午实操演练（3个真实case模拟，组长现场打分）<br>通过后：组长签署上岗确认单，正式进入team群</div>
      </div>
      <div class="train-item">
        <div class="train-label">笔试范围</div>
        <div class="train-text">四大黄金原则（默写）<br>CARP模型4步（默写）<br>品牌退换货政策（判断对错题）<br>升级机制4个触发条件（填空）<br>产品成分功效匹配题（3题）<br>话术模板应用题（2题，给场景写回复）</div>
      </div>
      <div class="train-item">
        <div class="train-label">实操考核标准</div>
        <div class="train-text">情绪处理：是否先用CARP安抚情绪（20分）<br>流程合规：是否按退换货流程处理（20分）<br>边界意识：是否未超权限承诺（20分）<br>产品建议：是否能给出合理产品搭配建议（20分）<br>升级判断：是否正确判断需要升级的case（20分）<br>总分80分及以上通过</div>
      </div>
      <div class="train-item">
        <div class="train-label">上岗后成长路径</div>
        <div class="train-text">Week 1-2：组长带教，每日复盘<br>Week 3-4：独立处理普通case，重大case上报<br>Month 2：开始处理复杂投诉，积累品牌群沟通经验<br>Month 3：考核晋升通道开放，可申请「高级售后专员」</div>
      </div>
    </div>
  </div>'''

# Insert after train10 closes
old_end = '''        <div class="train-items"><div class="train-item"><div class="train-label">考核内容</div><div class="train-text">① 背诵四大黄金原则（现场抽查）<br>② 独立完成5个模拟case（必须包含：愤怒投诉型+威胁曝光型）<br>③ 通过CARP模型场景演练<br>④ 品牌群申请格式测试（必须包含：证据+订单号+处理建议）</div></div><div class="train-item"><div class="train-label">考核通过标准</div><div class="train-text">5个模拟case中至少4个处理符合规范<br>话术模板能正确使用（不自行创造违规话术）<br>知道什么时候该升级，不独自硬扛</div></div><div class="train-item"><div class="train-label">上岗后支持</div><div class="train-text">前2周：组长带教，每个case做完后复盘<br>第3-4周：独立处理，组长监督<br>第5周起：独立上岗，重大case仍需上报</div></div><div class="train-item"><div class="train-label">持续学习</div><div class="train-text">每周案例分享会（讨论真实case）<br>每月话术库更新（根据新case添加）<br>品牌方政策变动时立即同步<br>遇到奇葩case立即记录并分享</div></div></div>
  </div>
    </div>
  </section>'''

new_end = '''        <div class="train-items"><div class="train-item"><div class="train-label">考核内容</div><div class="train-text">① 背诵四大黄金原则（现场抽查）<br>② 独立完成5个模拟case（必须包含：愤怒投诉型+威胁曝光型）<br>③ 通过CARP模型场景演练<br>④ 品牌群申请格式测试（必须包含：证据+订单号+处理建议）</div></div><div class="train-item"><div class="train-label">考核通过标准</div><div class="train-text">5个模拟case中至少4个处理符合规范<br>话术模板能正确使用（不自行创造违规话术）<br>知道什么时候该升级，不独自硬扛</div></div><div class="train-item"><div class="train-label">上岗后支持</div><div class="train-text">前2周：组长带教，每个case做完后复盘<br>第3-4周：独立处理，组长监督<br>第5周起：独立上岗，重大case仍需上报</div></div><div class="train-item"><div class="train-label">持续学习</div><div class="train-text">每周案例分享会（讨论真实case）<br>每月话术库更新（根据新case添加）<br>品牌方政策变动时立即同步<br>遇到奇葩case立即记录并分享</div></div></div>
  </div>
''' + product_training + '''
    </div>
  </section>'''

html = html.replace(old_end, new_end, 1)

# 4) Update CSS track-line gradient to span 7 dots
old_line = '.track-line {\n  position: absolute;\n  top: 50%;\n  left: 0;\n  right: 0;\n  height: 3px;\n  background: linear-gradient(90deg, #1A36A4 0%, #2B5BE8 50%, #E8F0FE 100%);\n  border-radius: 2px;\n  transform: translateY(-50%);\n}'
new_line = '.track-line {\n  position: absolute;\n  top: 50%;\n  left: 0;\n  right: 0;\n  height: 3px;\n  background: linear-gradient(90deg, #1A36A4 0%, #2B5BE8 33%, #2B5BE8 50%, #E8F0FE 80%);\n  border-radius: 2px;\n  transform: translateY(-50%);\n}'

html = html.replace(old_line, new_line, 1)

# 5) Add a note card after the timeline track about product training timing
product_timing_note = '''
  <div class="train-timing-note">
    <div class="note-icon">&#x2139;</div>
    <div class="note-text"><strong>关于产品培训时间安排的建议：</strong>产品知识培训建议安排在第6天，此时新人已掌握基础服务流程，可以把产品学习与流程操作结合理解。建议上午由品牌方产品负责人进行2小时宣讲，下午团队内部消化。考核通过后再安排跟组实习。</div>
  </div>'''

# Insert after the training track div
old_track_end = '''      </div>
      
  <div class="train-card" id="train01">'''

new_track_end = '''      </div>
      ''' + product_timing_note + '''
      
  <div class="train-card" id="train01">'''

html = html.replace(old_track_end, new_track_end, 1)

# 6) Add CSS for timing note
old_css_end = '''/* ====== RESPONSIVE ====== */
@media (max-width: 768px) {'''

new_css_end = '''/* ====== TRAINING TIMING NOTE ====== */
.train-timing-note {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  background: linear-gradient(135deg, #FFF8E6 0%, #FFF3CC 100%);
  border: 1px solid #FFD966;
  border-radius: 12px;
  padding: 14px 18px;
  margin: 20px 0 8px;
  max-width: 800px;
}
.note-icon {
  font-size: 20px;
  flex-shrink: 0;
  line-height: 1;
  margin-top: 2px;
}
.note-text {
  font-size: 13px;
  color: #6B5200;
  line-height: 1.7;
}
.note-text strong {
  color: #8B6914;
}

/* ====== RESPONSIVE ====== */
@media (max-width: 768px) {'''

html = html.replace(old_css_end, new_css_end, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Done! Output size: {len(html)} chars")
