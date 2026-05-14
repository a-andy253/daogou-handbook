#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild training section with Alra doc content integrated into 5-day plan."""
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ===== 1. Replace timeline track (7 dots -> 5 dots) =====
old_dots = '''          <div class="track-dot active" data-day="1">Day 1<br><small>认知<br>入门</small></div>
          <div class="track-dot" data-day="2">Day 2<br><small>情绪<br>流程</small></div>
          <div class="track-dot" data-day="3">Day 3<br><small>客户<br>话术</small></div>
          <div class="track-dot" data-day="4">Day 4<br><small>保护<br>协作</small></div>
          <div class="track-dot" data-day="5">Day 5<br><small>考核<br>上岗</small></div>
          <div class="track-dot" data-day="6">Day 6<br><small>产品<br>知识</small></div>
          <div class="track-dot" data-day="7">Day 7<br><small>最终<br>考核</small></div>'''

new_dots = '''          <div class="track-dot active" data-day="1">Day 1<br><small>认知<br>规范</small></div>
          <div class="track-dot" data-day="2">Day 2<br><small>情绪<br>流程</small></div>
          <div class="track-dot" data-day="3">Day 3<br><small>话术<br>FAQ</small></div>
          <div class="track-dot" data-day="4">Day 4<br><small>特殊<br>场景</small></div>
          <div class="track-dot" data-day="5">Day 5<br><small>考核<br>上岗</small></div>'''

html = html.replace(old_dots, new_dots, 1)

# ===== 2. Update header =====
html = html.replace(
    '7天系统学习，从入门到独立上岗',
    '5天系统学习，从入门到独立上岗（含Alra品牌话术）',
    1
)

# ===== 3. Replace timing note =====
old_note = '''  <div class="train-timing-note">
    <div class="note-icon">&#x2139;</div>
    <div class="note-text"><strong>关于产品培训时间安排的建议：</strong>产品知识培训建议安排在第6天，此时新人已掌握基础服务流程，可以把产品学习与流程操作结合理解。建议上午由品牌方产品负责人进行2小时宣讲，下午团队内部消化。考核通过后再安排跟组实习。</div>
  </div>'''

new_note = '''  <div class="train-timing-note">
    <div class="note-icon">&#x1F4DD;</div>
    <div class="note-text">本培训计划整合自团队<strong>售后场景拆解</strong>与<strong>Alra品牌售后询盘话术模板 v1.1</strong>，涵盖8大高频场景、标准话术、红线禁区与特殊场景处理。时间紧凑但内容完整，建议集中学习+当天实操演练。</div>
  </div>'''

html = html.replace(old_note, new_note, 1)

# ===== 4. Replace ALL train cards (Day 1-12) =====
# Find the boundaries
train_start = html.find('  <div class="train-card" id="train01">')
train_end = html.find('    </div>\n  </section>', train_start)

# If not found, try alternate
if train_start == -1:
    train_start = html.find('<div class="train-card" id="train01">')
if train_end == -1:
    train_end = html.rfind('    </div>\n  </section>')

print(f"Train section: {train_start} -> {train_end}")

# Build new 5-day training content
def nl(s): return s.replace('\n', '<br>')

new_training = '''
  <div class="train-card" id="train01">
    <div class="train-card-header">
      <div class="train-icon">&#x1F3E2;</div>
      <div class="train-meta">
        <div class="train-day">第1天 · 上午</div>
        <div class="train-title">品牌认知与团队定位</div>
        <div class="train-subtitle">明白自己是谁，知道边界在哪</div>
      </div>
    </div>
    <div class="train-items">
      <div class="train-item">
        <div class="train-label">团队定位</div>
        <div class="train-text">我们是粉丝与品牌之间的「中间协调方」—— 不是客服，不是品牌方，不是达人的代言人</div>
      </div>
      <div class="train-item">
        <div class="train-label">核心价值</div>
        <div class="train-text">帮粉丝解决问题，帮品牌维护口碑，帮达人留住信任</div>
      </div>
      <div class="train-item">
        <div class="train-label">四大黄金原则</div>
        <div class="train-text">&#x274C; 不承诺（未经品牌方确认）<br>&#x274C; 不传话（传话必须留记录）<br>&#x274C; 不让情绪升级<br>&#x274C; 保护自己（截图留证）</div>
      </div>
      <div class="train-item">
        <div class="train-label">常见误区</div>
        <div class="train-text">&#x274C; 「达人卖的东西达人负责」 → 达人只是渠道，赔付责任归品牌方<br>&#x274C; 「我能帮你申请」 → 你只能说「我帮您转达」<br>&#x274C; 「这个问题我能处理」 → 必须先问组长和品牌方</div>
      </div>
    </div>
  </div>

  <div class="train-card" id="train02">
    <div class="train-card-header">
      <div class="train-icon">&#x26A0;</div>
      <div class="train-meta">
        <div class="train-day">第1天 · 上午</div>
        <div class="train-title">红线禁区与自我保护</div>
        <div class="train-subtitle">哪些话绝对不能说，哪些事必须做</div>
      </div>
    </div>
    <div class="train-items">
      <div class="train-item">
        <div class="train-label">&#x1F6AB; 效果红线（绝对禁止）</div>
        <div class="train-text">&#x274C; 「绝对没问题」「保证能治好」「一个月就好了」「没有任何副作用」<br>统一改为：「因人而异，建议坚持4-8周观察」</div>
      </div>
      <div class="train-item">
        <div class="train-label">&#x1F6AB; 责任归属红线</div>
        <div class="train-text">&#x274C; 「那是你的问题」「别人用都没事」「我们产品没问题」<br>统一改为：「我帮你确认后回复」</div>
      </div>
      <div class="train-item">
        <div class="train-label">&#x1F6AB; 处理态度红线</div>
        <div class="train-text">&#x274C; 「不归我管」「我不知道」「处理不了」「你爱找谁找谁」<br>统一改为：「我帮你记录，转给对应同事跟进」</div>
      </div>
      <div class="train-item">
        <div class="train-label">&#x1F6AB; 过敏敷衍红线</div>
        <div class="train-text">&#x274C; 「这很正常，没事」「再观察两天」「建立耐受就是这样」<br>统一改为：「先停用，我会转给品牌团队处理」</div>
      </div>
      <div class="train-item">
        <div class="train-label">&#x1F6AB; 未经授权承诺红线</div>
        <div class="train-text">&#x274C; 「可以赔/可以退」（无权决定）<br>&#x274C; 「明天一定答复」「这个我说了算」<br>统一改为：「你的诉求我记下了，24小时内品牌团队会联系你」</div>
      </div>
      <div class="train-item">
        <div class="train-label">&#x1F6AB; 删除差评红线（违规）</div>
        <div class="train-text">&#x274C; 「麻烦删一下差评」「删了赔你」「删了给你退款」<br>合规话术：「感谢反馈，帮你解决问题后愿意的话帮忙更新评价，不强求」</div>
      </div>
      <div class="train-item">
        <div class="train-label">&#x1F6AB; 「应该是」高危禁区</div>
        <div class="train-text">&#x274C; 「应该是正常的」「应该是过敏」「应该问题不大」<br>猜测性回答 = 延误+不信任，一旦说错就完了。<br>&#x2705; 统一改为：「我帮你确认后回复」</div>
      </div>
      <div class="train-item">
        <div class="train-label">&#x1F512; 必须截图留证</div>
        <div class="train-text">需截图保存：辱骂/威胁/超出权限承诺/产品照片<br>文件名格式：[日期]_[品牌]_[粉丝ID]_[问题类型]_[处理结果]<br>保存期限：6个月</div>
      </div>
    </div>
  </div>

  <div class="train-card" id="train03">
    <div class="train-card-header">
      <div class="train-icon">&#x26A1;</div>
      <div class="train-meta">
        <div class="train-day">第1天 · 下午</div>
        <div class="train-title">响应标准与优先级判断</div>
        <div class="train-subtitle">3分钟内首次响应，30秒内分类判断</div>
      </div>
    </div>
    <div class="train-items">
      <div class="train-item">
        <div class="train-label">响应时效标准</div>
        <div class="train-text">P0紧急（威胁曝光/涉及安全） → 4小时内专人联系<br>P1紧急投诉 → 立即上报<br>P2重要投诉 → 2小时内处理<br>P3普通咨询 → 24小时内回复<br>P4常规 → 下一个工作日</div>
      </div>
      <div class="train-item">
        <div class="train-label">首次响应模板（30秒必回）</div>
        <div class="train-text">宝子！我看到啦 &#x1F64C; 先别急，跟我说说怎么了？你说的情况我记下来了，一定帮你处理到底！<br><br>&#x274C; 禁止开头：「请问您遇到了什么问题？」（太正式）<br>&#x274C; 禁止：「您好，看到您的反馈了」（像机器人）<br>&#x274C; 禁止：直接发产品链接或自动回复（零温度）</div>
      </div>
      <div class="train-item">
        <div class="train-label">情绪激动用户安抚模板</div>
        <div class="train-text">宝子别急，我懂你的心情 &#x1F614; 先深呼吸一下，我在这里陪你处理，不解决不罢休 &#x2764; 来，慢慢跟我说，我们一起想办法<br><br>技巧：承认情绪，不辩解（「你说得对，这种情况确实不应该发生」）<br>&#x274C; 避免：「你先冷静一下」（会让人更激动）</div>
      </div>
      <div class="train-item">
        <div class="train-label">多问题并发处理</div>
        <div class="train-text">&#x26A0; 适用：用户一口气提3个以上问题<br>&#x2705; 模板：「宝子，问题我都记下来了，一个个给你处理 &#x1F4AA; 按紧急程度来，先处理[最紧急的]，然后[次要的]，最后[其他的]。我们先搞第一个，好吗？」<br><br>不要碎片化回复（分开回显得在敷衍）<br>用数字编号让用户感觉被认真对待<br>解决一个主动说「搞定了，继续下一个」</div>
      </div>
    </div>
  </div>

  <div class="train-card" id="train04">
    <div class="train-card-header">
      <div class="train-icon">&#x1F9D8;</div>
      <div class="train-meta">
        <div class="train-day">第2天 · 上午</div>
        <div class="train-title">客诉调查七步法（核心流程）</div>
        <div class="train-subtitle">Alra标准流程，每一步都有话术</div>
      </div>
    </div>
    <div class="train-items">
      <div class="train-item">
        <div class="train-label">第一步：礼貌接待，建立信任</div>
        <div class="train-text">&#x2705; 话术：「宝子你好！谢谢你愿意跟我说 &#x1F64F; 你先别担心，我仔细听，慢慢说，我全程都在～」</div>
      </div>
      <div class="train-item">
        <div class="train-label">第二步：深入了解，挖掘需求</div>
        <div class="train-text">&#x2705; 话术：「为了帮你搞准确，先问你几个关键问题：你描述得越细，我越能帮你判断原因哦～」<br><br>追问技巧：开放式引导（「能具体说说是什么感觉吗？」）<br>确认细节（「是右边脸颊，还是两边都有？」）<br>&#x274C; 避免：「你是不是没用对方法？」（像在推责任）</div>
      </div>
      <div class="train-item">
        <div class="train-label">第三步+第四步：同步交叉执行</div>
        <div class="train-text">&#x26A0; 说明：追溯肤质和分析用法在实际对话中同时进行、灵活切换，跟着用户自然节奏走，核心是快速收集信息，不要让用户感觉在被审问。<br><br>&#x2705; 话术：「帮你分析一下，再问你几个问题：关于肤质：[追问] 关于用法：[追问]」</div>
      </div>
      <div class="train-item">
        <div class="train-label">第五步：提供建议，解释原理</div>
        <div class="train-text">&#x2705; 话术：「看了一下你的情况，我的建议是：【这么做】[具体方案]【为什么】因为……（用大白话解释原理）你按这个试3-5天，有好转就继续，变得更严重的话马上告诉我！」</div>
      </div>
      <div class="train-item">
        <div class="train-label">第六步：识别红线，立刻上报</div>
        <div class="train-text">&#x1F6A8; 遇到这些情况，立刻上报，不要自己扛：<br>· 出现水疱/渗液/严重红肿<br>· 粉丝威胁找媒体/监管部门<br>· 超过权限的赔偿要求<br><br>&#x2705; 话术：「宝子，你说的这种情况需要我们品牌专业团队来处理，我会马上把你的情况转过去，你按以下步骤先做：①停用这款产品 ②清水轻轻洗，不用洗面奶 ③出现[具体症状]立刻去医院。我今天内把你的情况提交给品牌团队，24小时内他们会直接联系你。」<br><br>&#x274C; 禁止说：「这只是正常反应，没事」「再观察两天看看」「处理不了」「应该是……」</div>
      </div>
      <div class="train-item">
        <div class="train-label">第七步：统一口径，专业沟通</div>
        <div class="train-text">对外宣传三原则（必须记住）：<br><strong>成分你最懂</strong> — 对产品成分的理解和选择，说出专业感<br><strong>检测关最严</strong> — 远超行业标准的多重检测，说出安全感<br><strong>合规专家审</strong> — 所有物料经过合规团队审核，说出信任感</div>
      </div>
    </div>
  </div>

  <div class="train-card" id="train05">
    <div class="train-card-header">
      <div class="train-icon">&#x1F504;</div>
      <div class="train-meta">
        <div class="train-day">第2天 · 下午</div>
        <div class="train-title">退换货流程与品牌沟通规范</div>
        <div class="train-subtitle">所有退换货必须通过品牌群申请</div>
      </div>
    </div>
    <div class="train-items">
      <div class="train-item">
        <div class="train-label">判断标准</div>
        <div class="train-text">未开封+7天内 → 支持<br>已开封+有质量问题 → 支持（需证据）<br>已开封+无质量问题 → 不支持（可申请补偿）<br>已过期 → 不支持（可申请人情补偿）</div>
      </div>
      <div class="train-item">
        <div class="train-label">申请流程</div>
        <div class="train-text">确认订单 → 确认产品状态 → 判断是否在品牌支持范围 → 在品牌群申请（附：证据+订单号+处理建议）→ 等待审批（24-48小时）→ 反馈粉丝</div>
      </div>
      <div class="train-item">
        <div class="train-label">品牌群沟通格式</div>
        <div class="train-text">@品牌方 / 问题描述 / 产品状态 / 粉丝诉求 / 申请处理方式 / 附证据<br><br>永远不能在品牌群外私下承诺粉丝处理结果</div>
      </div>
      <div class="train-item">
        <div class="train-label">重要提醒</div>
        <div class="train-text">粉丝问「能不能退」 → 只能说「我帮您申请」<br>品牌方回复后才能给粉丝最终答复<br>没有品牌方回复，不能给任何实质性承诺</div>
      </div>
    </div>
  </div>

  <div class="train-card" id="train06">
    <div class="train-card-header">
      <div class="train-icon">&#x1F4AC;</div>
      <div class="train-meta">
        <div class="train-day">第3天 · 上午</div>
        <div class="train-title">高频场景FAQ话术（上）</div>
        <div class="train-subtitle">场景1-4：产品功效 / 过敏 / 使用 / 破损</div>
      </div>
    </div>
    <div class="train-items">
      <div class="train-item">
        <div class="train-label">场景1 · 产品功效咨询</div>
        <div class="train-text"><strong>Q：这款产品能去皱吗？</strong><br>&#x2705; 「这款含高纯度玻色因，能促进胶原蛋白生成、改善细纹，经过第三方权威机构功效验证，坚持用有助延缓老化。每个人肤质不同，效果因人而异，建议坚持用4-8周看看变化 &#x1F60A;」<br><br><strong>Q：为什么比别家的贵？</strong><br>&#x2705; 「好问题！Alra坚持高品质进口原料，每一批次都经过远超行业标准的多重检测，这份投入只为给你带来真正安心有效的护肤体验。护肤品和普通商品不一样，成分纯度、稳定性、配方科学性都直接影响效果和安全性，我们宁愿在源头多投入，也不想让你的皮肤承担风险。」<br><br>&#x274C; 禁止：「因为我们是大牌啊」「便宜没好货」</div>
      </div>
      <div class="train-item">
        <div class="train-label">场景2 · 过敏/疑似过敏</div>
        <div class="train-text"><strong>Q：我用完过敏了！</strong><br>&#x2705; 「宝子，真的很抱歉！先别急：<br>1. 停用产品，不要再涂了<br>2. 用清水轻轻洗脸，什么都不要抹<br>3. 观察24小时，如果出现水疱/渗液/肿得更厉害，或者身体不舒服，立刻去医院。你的情况我会马上转给品牌专业团队，24小时内他们会联系你全程跟进 &#x1F64F;」<br><br><strong>Q：这个产品安全吗？会烂脸吗？</strong><br>&#x2705; 「宝子问得好，说明你对自己皮肤很负责 &#x1F4AA; Alra每款产品都经过严格质检和安全评估，符合国家化妆品标准。护肤反应因人而异，就像有人对芒果过敏、有人对海鲜过敏，这是个人差异，不是产品本身有问题。」</div>
      </div>
      <div class="train-item">
        <div class="train-label">场景3 · 产品使用疑问</div>
        <div class="train-text"><strong>Q：用了脸红是正常的吗？</strong><br>情况A（轻微泛红+30分钟内消退）：「用完轻微泛红是果酸的正常反应哦～ 说明产品里的活性成分在起作用，促进老废角质代谢。30分钟内会自然消退，不用担心 &#x1F60A;」<br>情况B（泛红超1小时或刺痛）：「这种情况说明你皮肤对这款产品还没建立耐受，先暂停2-3天，等皮肤缓过来。初次使用一定要先少量上脸……」<br><br><strong>Q：需要建立耐受，怎么建？</strong><br>&#x2705; 「第1-2周：黄豆大小，全脸薄涂，停留3-5分钟后清水洗掉，隔2-3天用一次<br>第3-4周：停留时间延长到10分钟，观察皮肤状态<br>第4周以后：无不舒服可以尝试过夜。<br>过程中轻微刺痛或脱皮是正常的，减少用量或拉长间隔就好。出现明显红肿水疱，立刻停用联系我。」<br><br><strong>Q：用了还能用维A醇吗？</strong><br>&#x26A0; 「维A醇和果酸最好不要一起用，两个叠加刺激性会增强，容易出现泛红/脱皮/刺痛。建议搭配方案：[早C晚A分时使用，或先用果酸2-3周再引入维A醇]」</div>
      </div>
      <div class="train-item">
        <div class="train-label">场景4 · 产品破损/保质期</div>
        <div class="train-text"><strong>Q：收到产品破损了/漏液了</strong><br>&#x2705; 「宝子，收到破损真的很抱歉 &#x1F614; 别急，我帮你处理！麻烦你先做两件事：①拍照（产品+包装）②发一下订单号。核实之后我们可以免运费补发新的，或者补偿你一张优惠券，可以吗？真的非常抱歉 &#x1F64F;」<br><br><strong>Q：产品保质期/生产日期怎么查？</strong><br>&#x2705; 「好问题！Alra产品批次信息透明可查 &#x1F4CB; 你看一下外包装：[说明查看位置]。如果看不清，告诉我产品名和批号，我帮你查 &#x1F60A;」</div>
      </div>
    </div>
  </div>

  <div class="train-card" id="train07">
    <div class="train-card-header">
      <div class="train-icon">&#x1F4AC;</div>
      <div class="train-meta">
        <div class="train-day">第3天 · 下午</div>
        <div class="train-title">高频场景FAQ话术（下）</div>
        <div class="train-subtitle">场景5-8：质疑对比 / 效果 / 赔偿 / 删评</div>
      </div>
    </div>
    <div class="train-items">
      <div class="train-item">
        <div class="train-label">场景5 · 质疑/对比类</div>
        <div class="train-text"><strong>Q：网上有人说你们产品有问题？</strong><br>&#x2705; 「谢谢宝子愿意告诉我们 &#x1F64F; 我们始终坚持「成分懂、检测严、合规审」原则，对产品品质负责到底。如果你看到的是具体信息，辛苦发给我：[请用户提供链接/截图]。我们会立即认真核查，有结果第一时间告诉你。如果确实是我们的问题，绝不回避，负责到底 &#x1F4AA;」<br><br><strong>Q：别人用了怎么没事？</strong><br>&#x2705; 「您观察得很仔细！确实存在个体差异，就像有人喝牛奶不舒服，有人完全没问题，是肤质不同，不是产品的问题 &#x1F60A; 你用后的情况我会认真记录，反馈给产品配方团队。如果你愿意多说说你用后的具体情况，我可以帮你分析 &#x1F64F;」<br><br><strong>Q：我皮肤能用好吗？</strong><br>&#x2705; 「谢谢信任！按你描述的肤质，理论上适合你，但因为个体差异，建议：如果你以前有过敏史，或者现在皮肤正处于敏感状态，建议先用温和产品稳定皮肤，再考虑功效型产品哦～」<br>&#x274C; 禁止：「放心，绝对没问题！」</div>
      </div>
      <div class="train-item">
        <div class="train-label">场景6 · 使用效果类</div>
        <div class="train-text"><strong>Q：用了没效果怎么办？</strong><br>情况A（使用不足4周）：「宝子，功效型护肤品一般要坚持用才能看到效果 &#x1F60A; 皮肤代谢周期28天左右，建议：[鼓励坚持+检查用法] 你用了多久了？说说使用感受，我帮你分析。」<br><br>情况B（超过8周仍无明显效果）：「宝子，理解你的心情，用了这么久看不到效果确实会着急 &#x1F4AA; 不过用这么久没感觉到变化，通常有两种情况，我们来一个个排查：<br>B1：其实有效果，但没感知到（润物细无声）。<br>B2：产品确实不适合你，需要调整。<br>帮我回答几个问题：[用量/搭配/目标困扰]。你说的情况我会反馈给品牌团队，帮你分析要不要调整用法或者换方案 &#x1F64F;」<br><br><strong>拍照对比法</strong>（最常见被忽略的场景）：「宝子，先别急着下结论，来做个小测试：打开手机相册，找一张用之前的脸部照片，关掉美颜和滤镜，跟现在的脸对比一下——有没有发现：[光泽/痘印/吸收/稳定/出油] 有以上任意一点，那就是有效果，只是变化比较细，每天看镜子不容易发现。」</div>
      </div>
      <div class="train-item">
        <div class="train-label">场景7 · 赔偿/退款诉求</div>
        <div class="train-text">&#x2705; 「宝子，我理解你的心情，真的很抱歉带来了不便 &#x1F64F; 赔偿/退款这个我没权限直接答应，但我把你的诉求完整记下来，马上提交给客服主管和品牌团队。会在24小时内与你联系，沟通具体方案。这段时间辛苦留意抖音消息，方便他们联系你。如果比较紧急，我帮你催一下优先处理。」<br><br>&#x274C; 禁止：「可以赔/可以退」（无权决定）<br>&#x274C; 禁止：「这不归我管」（推诿）</div>
      </div>
      <div class="train-item">
        <div class="train-label">场景8 · 删除差评诉求（高风险）</div>
        <div class="train-text">&#x2705; 「宝子，看到你的反馈了，真的很抱歉给你带来了不好的体验 &#x1F614; 对于大家评论，每条我们都会认真对待 &#x1F64F; 关于你反馈的问题，我们希望能直接和你沟通，彻底帮你解决：[提供联系方式]。如果处理完你满意了，愿意的话帮忙更新一下评价？不强求，只是真心希望帮你解决问题 &#x1F4AA;」<br><br>&#x274C; 禁止：直接说「删一下差评」/ 「删了赔你」/ 「删了给你退款」</div>
      </div>
    </div>
  </div>

  <div class="train-card" id="train08">
    <div class="train-card-header">
      <div class="train-icon">&#x1F6D1;</div>
      <div class="train-meta">
        <div class="train-day">第4天 · 上午</div>
        <div class="train-title">特殊场景处理与升级机制</div>
        <div class="train-subtitle">不能按常规流程处理的情况</div>
      </div>
    </div>
    <div class="train-items">
      <div class="train-item">
        <div class="train-label">场景A · 用户要求赔偿/退款</div>
        <div class="train-text">不当场答应，先安抚+升级，24小时内回复<br>&#x2705; 话术：「我理解你的心情，你的诉求我记下来了，会第一时间提交给品牌团队处理，24小时内会有人联系你。」</div>
      </div>
      <div class="train-item">
        <div class="train-label">场景B · 用户威胁投诉（监管/媒体）</div>
        <div class="train-text">&#x1F6A8; 立刻标记P0紧急，4小时内部门负责人或更高级别专人联系<br>&#x2705; 话术：「我理解您希望问题得到重视。我们会认真对待每一位顾客的反馈，争取尽快给您一个满意的处理方案。我这边会立刻上报，稍后会有专人联系您。」</div>
      </div>
      <div class="train-item">
        <div class="train-label">场景C · 用户要求删除差评（高风险）</div>
        <div class="train-text">&#x26A0; 不能要求删评，不能用赔偿诱导删评<br>&#x2705; 合规话术：「感谢反馈，我们会认真处理，你满意的话愿意的话帮忙更新评价，不强求。」</div>
      </div>
      <div class="train-item">
        <div class="train-label">场景D · 用户辱骂/人身攻击</div>
        <div class="train-text">保持专业，截图留证，标记跟进<br>不要回骂，不要激化，冷静处理<br>如持续攻击可暂时离开工位休息</div>
      </div>
      <div class="train-item">
        <div class="train-label">场景E · 老客户重复投诉</div>
        <div class="train-text">查阅历史记录，避免重复提问<br>再次回复时先确认：「宝子，上次的问题处理到哪一步了？我们继续跟进」<br>不要让用户重复叙述同一问题</div>
      </div>
      <div class="train-item">
        <div class="train-label">升级触发条件</div>
        <div class="train-text">&#x2B06;&#xFE0F; 同一问题被投诉2次以上<br>&#x2B06;&#xFE0F; 粉丝威胁曝光 / 投诉平台 / 报警<br>&#x2B06;&#xFE0F; 处理时间超过48小时未解决<br>&#x2B06;&#xFE0F; 涉及金额超过500元<br>&#x2B06;&#xFE0F; 涉及产品质量安全问题（可能舆情）<br>&#x2B06;&#xFE0F; 品牌方72小时内未回应</div>
      </div>
      <div class="train-item">
        <div class="train-label">万能脱身句（不知道怎么说时）</div>
        <div class="train-text">「宝子，你这个问题比较专业，我要先确认一下细节 &#x1F64F; 我先记下来，稍后给你准确的回复，好吗？一般1-2小时，一定第一时间联系你。」</div>
      </div>
    </div>
  </div>

  <div class="train-card" id="train09">
    <div class="train-card-header">
      <div class="train-icon">&#x1F6AB;</div>
      <div class="train-meta">
        <div class="train-day">第4天 · 下午</div>
        <div class="train-title">难缠客户应对与无理取闹处理</div>
        <div class="train-subtitle">五不原则 + 10种客户分类</div>
      </div>
    </div>
    <div class="train-items">
      <div class="train-item">
        <div class="train-label">五不原则（处理无理取闹/恶意用户）</div>
        <div class="train-text">&#x274C; 不对骂 — 保持专业，不激化矛盾<br>&#x274C; 不承诺 — 超出权限的不答应<br>&#x274C; 不过多解释 — 3次无效停止纠缠<br>&#x274C; 不单独扛 — 立刻上报组长<br>&#x274C; 不留把柄 — 截图保存所有对话</div>
      </div>
      <div class="train-item">
        <div class="train-label">愤怒投诉型</div>
        <div class="train-text">特征：用感叹号、多条消息轰炸、要求立即处理<br>&#x2705; 话术：「我理解您的感受，我这就帮您协调处理，预计[时间]内给您回复」<br>&#x274C; 避坑：不要争论对错，不要说「不归我们管」</div>
      </div>
      <div class="train-item">
        <div class="train-label">威胁曝光型</div>
        <div class="train-text">特征：「我要发帖曝光」 / 「我要投诉平台」<br>&#x2705; 话术：「我理解您希望问题得到重视的心情，我们会认真对待每一位顾客的反馈」<br>&#x274C; 避坑：不因威胁而让步，但态度不能变硬</div>
      </div>
      <div class="train-item">
        <div class="train-label">无理取闹型</div>
        <div class="train-text">特征：开封后退/过期后退/赠品要求超出政策<br>&#x2705; 话术：先肯定情绪 → 说明品牌方政策（用「品牌方规定」而非「我们规定」）→ 给替代方案<br>&#x274C; 避坑：不给对抗，给台阶</div>
      </div>
      <div class="train-item">
        <div class="train-label">多人串联型（舆情高危）</div>
        <div class="train-text">特征：同一问题多人集中反馈<br>&#x2705; 话术：每个粉丝都当作唯一case处理，回复不提「多人」<br>&#x274C; 避坑：永远不要说「别人也有这个问题」——会让普通投诉升级成集体维权</div>
      </div>
      <div class="train-item">
        <div class="train-label">其余5种</div>
        <div class="train-text">&#x2774; 反复纠缠型 — 不重复给相同答案，引导看之前的回复记录<br>&#x2775; 情感脆弱型 — 优先处理情绪，再处理问题<br>&#x2776; 专业质问型 — 不懂就说「我确认后回复」，不瞎猜<br>&#x2777; 找领导型 — 「我理解，我安排组长跟进，方案确认后通过大管家账号联系您」<br>&#x2778; 沉默抗拒型 — 给出明确时限，让用户知道有人在跟进</div>
      </div>
    </div>
  </div>

  <div class="train-card" id="train10">
    <div class="train-card-header">
      <div class="train-icon">&#x1F3C6;</div>
      <div class="train-meta">
        <div class="train-day">第5天</div>
        <div class="train-title">综合考核与上岗评估</div>
        <div class="train-subtitle">通过考核，正式成为团队一员</div>
      </div>
    </div>
    <div class="train-items">
      <div class="train-item">
        <div class="train-label">考核安排</div>
        <div class="train-text">上午笔试（产品知识+服务规范，60分及格）<br>下午实操演练（3个真实case模拟，组长现场打分）<br>通过后：组长签署上岗确认单，正式进入team群</div>
      </div>
      <div class="train-item">
        <div class="train-label">笔试范围</div>
        <div class="train-text">四大黄金原则（默写）<br>红线禁区（判断对错题）<br>7步客诉调查法（填空）<br>升级机制4个触发条件（填空）<br>8大场景话术应用题（给场景写回复）<br>「应该是」禁区统一改为（填空）</div>
      </div>
      <div class="train-item">
        <div class="train-label">实操考核标准（5项×20分=100分）</div>
        <div class="train-text">情绪处理：是否先用CARP安抚情绪（20分）<br>流程合规：是否按7步法+退换货流程处理（20分）<br>红线意识：是否未触碰禁区/超权限承诺（20分）<br>话术应用：8大场景话术是否正确使用（20分）<br>升级判断：是否正确判断需要升级的case（20分）<br>总分80分及以上通过</div>
      </div>
      <div class="train-item">
        <div class="train-label">上岗后成长路径</div>
        <div class="train-text">Week 1-2：组长带教，每日复盘<br>Week 3-4：独立处理普通case，重大case上报<br>Month 2：开始处理复杂投诉，积累品牌群沟通经验<br>Month 3：考核晋升通道开放，可申请「高级售后专员」</div>
      </div>
    </div>
  </div>
'''

# Replace old training content with new
if train_start > 0 and train_end > train_start:
    html = html[:train_start] + new_training + html[train_end:]
    print(f"Replaced training section ({train_end - train_start} chars -> {len(new_training)} chars)")
else:
    print(f"ERROR: Could not find boundaries. start={train_start}, end={train_end}")

# Update CSS track-line gradient back to 5 dots
old_line = '.track-line {\n  position: absolute;\n  top: 50%;\n  left: 0;\n  right: 0;\n  height: 3px;\n  background: linear-gradient(90deg, #1A36A4 0%, #2B5BE8 33%, #2B5BE8 50%, #E8F0FE 80%);\n  border-radius: 2px;\n  transform: translateY(-50%);\n}'
new_line = '.track-line {\n  position: absolute;\n  top: 50%;\n  left: 0;\n  right: 0;\n  height: 3px;\n  background: linear-gradient(90deg, #1A36A4 0%, #2B5BE8 50%, #E8F0FE 100%);\n  border-radius: 2px;\n  transform: translateY(-50%);\n}'
html = html.replace(old_line, new_line, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Done! Output size: {len(html)} chars")
