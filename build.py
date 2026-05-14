#!/usr/bin/env python3
"""Generate complete handbook HTML."""
import re, json

# Read original handbook
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Load data from JSON
with open('scenarios.json', 'r', encoding='utf-8') as f:
    scenes = json.load(f)

# Training data (no Chinese quotes, safe)
training = [
    {
        "num": "01", "icon": "🏢", "title": "品牌认知与团队定位",
        "subtitle": "明白自己是谁，知道边界在哪", "duration": "1",
        "items": [
            {"label": "团队定位", "text": "我们是粉丝与品牌之间的「中间协调方」—— 不是客服，不是品牌方，不是达人的代言人"},
            {"label": "核心价值", "text": "帮粉丝解决问题，帮品牌维护口碑，帮达人留住信任"},
            {"label": "四大黄金原则", "text": "① 不承诺（未经品牌方确认）\n② 不传话（传话必须留记录）\n③ 不让情绪升级\n④ 保护自己（截图留证）"},
            {"label": "常见误区", "text": "❌ 「达人卖的东西达人负责」 → 达人只是渠道，赔付责任归品牌方\n❌ 「我能帮你申请」 → 你只能说「我帮您转达」\n❌ 「这个问题我能处理」 → 必须先问组长和品牌方"}
        ]
    },
    {
        "num": "02", "icon": "⚡", "title": "响应标准与优先级判断",
        "subtitle": "3分钟内首次响应，30秒内分类判断", "duration": "1",
        "items": [
            {"label": "响应时效", "text": "P1紧急投诉 → 立即上报\nP2重要投诉 → 2小时内处理\nP3普通咨询 → 24小时内回复\nP4常规 → 下一个工作日"},
            {"label": "首次响应模板", "text": "亲爱的[名字]，感谢您的留言～我是[达人]直播间的售后小助手，很高兴为您服务！您的问题我收到了，我这边帮您查询一下，稍后给您准确回复哦"},
            {"label": "分类判断", "text": "看到消息 → 30秒内判断类型（投诉/咨询/求情/威胁）→ 贴标签 → 按优先级处理"},
            {"label": "禁止行为", "text": "❌ 超过3分钟无响应\n❌ 首次回复说「我问问」\n❌ 同一个问题被问了2次以上还没解决"}
        ]
    },
    {
        "num": "03", "icon": "🧠", "title": "CARP情绪处理模型",
        "subtitle": "所有投诉必走的4步处理法", "duration": "2",
        "items": [
            {"label": "C - Control 掌控节奏", "text": "不被客户情绪带着走。语速放慢，回复间隔适当，先听完语音再判断情绪。不要用「您不要激动」这类话"},
            {"label": "A - Acknowledge 认可情绪", "text": "必须说出口（至少选一句）：\n「我完全理解您的感受」\n「换作是我也会着急」\n「您的心情我非常理解」"},
            {"label": "R - Refocus 转向解决", "text": "把话题从「谁对谁错」拉回到「怎么解决」。不要争论，不要解释为什么，先说「我理解」，再给方案"},
            {"label": "P - Problem Solve 着手解决", "text": "有方案 → 立即给出时间节点\n无方案 → 承诺「我会在XX时间给您回复」\n绝不说「我再帮你问问」然后不了了之"}
        ]
    },
    {
        "num": "04", "icon": "🔄", "title": "退换货流程与品牌沟通",
        "subtitle": "所有退换货必须通过品牌群申请", "duration": "2",
        "items": [
            {"label": "判断标准", "text": "未开封+7天内 → 支持\n已开封+有质量问题 → 支持（需证据）\n已开封+无质量问题 → 不支持（可申请补偿）\n已过期 → 不支持（可申请人情补偿）"},
            {"label": "申请流程", "text": "确认订单 → 确认产品状态 → 判断是否在品牌支持范围 → 在品牌群申请（附：证据+订单号+处理建议）→ 等待审批（24-48小时）→ 反馈粉丝"},
            {"label": "品牌群沟通", "text": "格式：@品牌方 / 问题描述 / 产品状态 / 粉丝诉求 / 申请处理方式 / 附证据\n永远不能在品牌群外私下承诺粉丝处理结果"},
            {"label": "重要提醒", "text": "粉丝问「能不能退」 → 只能说「我帮您申请」\n品牌方回复后才能给粉丝最终答复\n没有品牌方回复，不能给任何实质性承诺"}
        ]
    },
    {
        "num": "05", "icon": "🔟", "title": "10种难缠客户分类应对",
        "subtitle": "每种类型的特征、话术、避坑指南", "duration": "3",
        "items": [
            {"label": "愤怒投诉型", "text": "特征：用感叹号、语音轰炸、要求立即处理\n话术：「我理解您的感受，我这就帮您协调处理，预计[时间]内给您回复」\n避坑：不要争论对错，不要说「不归我们管」"},
            {"label": "威胁曝光型", "text": "特征：「我要发帖曝光」 / 「我要投诉平台」\n话术：「我理解您希望问题得到重视的心情，我们会认真对待每一位顾客的反馈」\n避坑：不因威胁而让步，但态度不能变硬"},
            {"label": "无理取闹型", "text": "特征：开封后退 / 过期后退 / 赠品要求超出政策\n话术：先肯定情绪 → 说明品牌方政策（用「品牌方规定」而非「我们规定」）→ 给替代方案\n避坑：不给对抗，给台阶"},
            {"label": "多人串联型（舆情高危）", "text": "特征：同一问题多人集中反馈\n话术：每个粉丝都当作唯一case处理，回复不提「多人」\n避坑：永远不要说「别人也有这个问题」——这句话会让普通投诉升级成集体维权"},
            {"label": "其余5种", "text": "④反复纠缠型 ⑤情感脆弱型 ⑥专业质问型 ⑦找领导型 ⑧沉默抗拒型\n详见完整版手册第四章"}
        ]
    },
    {
        "num": "06", "icon": "💬", "title": "话术模板实战练习",
        "subtitle": "熟记15个核心话术，随身携带的「说明书」", "duration": "3",
        "items": [
            {"label": "安抚情绪", "text": "「我完全理解您的感受，换作是我也会着急。请您放心，我一定会认真处理这件事。」"},
            {"label": "投诉质疑品牌", "text": "「您说得有道理，我这边帮您记录并反馈给品牌方。」"},
            {"label": "客户多次投诉", "text": "「感谢您再次联系我们，我理解您还没有得到满意的解决方案，我会亲自跟进。」"},
            {"label": "威胁曝光", "text": "「我理解您希望问题得到重视的心情。我们会认真对待每一位顾客的反馈，争取尽快给您一个满意的处理方案。」"},
            {"label": "要求找领导", "text": "「我完全理解您希望得到更多支持的心情。我会安排组长直接联系您，请问您方便接听电话的时间是？」"},
            {"label": "粉丝问「是不是很多人都遇到」", "text": "「亲爱的，我这边每天都会收到很多不同粉丝的咨询，每个人遇到的情况都不太一样，所以我会认真对待每一位粉丝的问题。」"},
            {"label": "被骂「骗子同伙」", "text": "「我非常理解您的心情，我们会认真对待每一位顾客的反馈，争取尽快给您一个满意的处理方案。请问您方便提供一下具体的订单信息吗？」"},
            {"label": "粉丝追问「为什么问这么多」", "text": "「申请赔偿需要了解具体情况，这样我才能帮您申请到对应的补偿方案，这是正常流程，请理解。」"},
            {"label": "无法立即解决", "text": "「您的情况我已经详细记录了，我会在[时间]前给您一个明确的回复，请耐心等待。」"},
            {"label": "结束语（任意场景）", "text": "「您这个问题我一定会认真跟进到底的 💕 如有任何疑问随时联系我，祝您生活愉快！」"}
        ]
    },
    {
        "num": "07", "icon": "🛡️", "title": "自我保护与边界意识",
        "subtitle": "保护自己，才能长期服务好客户", "duration": "4",
        "items": [
            {"label": "必须截图留证", "text": "所有投诉对话截图（保存6个月）\n品牌群申请和回复截图\n升级决策审批记录\n补偿/退款操作记录\n\n文件名格式：[日期]_[品牌]_[粉丝ID]_[问题类型]_[处理结果]"},
            {"label": "涉及录音/截图的case", "text": "立即截图留证 → 停止私下沟通 → 上报组长\n客服不单独回应，不解释，不道歉\n统一口径由组长或达人团队出面"},
            {"label": "不可突破的底线", "text": "❌ 不得自行承诺退款金额（必须品牌方确认）\n❌ 不得泄露粉丝个人信息给品牌方（或反之）\n❌ 不得以「我是帮你」为由做超出权限的承诺\n❌ 不得在情绪激动时做决定"},
            {"label": "情绪管理", "text": "客户语言攻击 ≠ 真的在骂你个人（对事不对人）\n遇到人身攻击可申请暂时离开工位\n每天有「吐槽时间」（15分钟可选参与）\n感到委屈可以找组长或同事倾诉"}
        ]
    },
    {
        "num": "08", "icon": "⬆️", "title": "升级机制与协作规范",
        "subtitle": "什么时候该上报，如何高效协作", "duration": "4",
        "items": [
            {"label": "升级触发条件", "text": "⬆️ 同一问题被投诉2次以上\n⬆️ 粉丝威胁曝光 / 投诉平台 / 报警\n⬆️ 处理时间超过48小时未解决\n⬆️ 涉及金额超过500元\n⬆️ 涉及产品质量安全问题（可能舆情）\n⬆️ 品牌方72小时内未回应"},
            {"label": "每日例会", "text": "早上9:00 → 昨日遗留case跟进 + 今日重点（各组员）\n下午16:00 → 今日新case汇总 + 品牌方反馈同步（Andy/组长）\n不定期 → 难缠case复盘讨论（存档形成话术库）"},
            {"label": "组长职责", "text": "对外品牌对接\n内部调度分配\n特殊case决策（金额>500/超权限）\n危机舆情预判与处理\n每周质检（抽查每人10条对话）"},
            {"label": "新人Q&A", "text": "Q：不确定能不能答应粉丝怎么办？\nA：先说「我帮您记录，稍后回复」，再问组长\n\nQ：粉丝骂我很难听怎么办？\nA：截图留证，等冷静后再处理，不要当场回骂\n\nQ：品牌方不回复怎么办？\nA：等48小时，超时上报组长启动催促机制"}
        ]
    },
    {
        "num": "09", "icon": "📊", "title": "KPI与绩效考核",
        "subtitle": "做得好有奖励，做不好有改进方向", "duration": "5",
        "items": [
            {"label": "月度KPI指标", "text": "首次响应时间 ≤ 3分钟\n问题解决率 ≥ 85%（不升级到组长）\n平均处理时长 ≤ 24小时\n客户满意度 ≥ 90%（好评率）\n品牌方投诉率 = 0"},
            {"label": "每周质检", "text": "随机抽查每人10条对话\n重点检查：情绪管理 / 话术规范 / 流程合规\n优秀案例归档到话术库，分享学习\n质检结果不公开通报，作为改进参考"},
            {"label": "奖励机制", "text": "🏅 每月「服务之星」（客户好评最多者）\n📋 季度最佳案例分享会\n⭐ 连续3个月KPI达标 → 优先安排品牌方参观学习机会"},
            {"label": "改进机制", "text": "连续2个月KPI未达标 → 组长一对一辅导\n连续3个月未达标 → 调整岗位或重新培训\n每月case复盘会，汇总常见问题，更新手册"}
        ]
    },
    {
        "num": "10", "icon": "🚀", "title": "新人实操与独立上岗",
        "subtitle": "模拟真实场景，通过考核后正式上岗", "duration": "5",
        "items": [
            {"label": "考核内容", "text": "① 背诵四大黄金原则（现场抽查）\n② 独立完成5个模拟case（必须包含：愤怒投诉型+威胁曝光型）\n③ 通过CARP模型场景演练\n④ 品牌群申请格式测试（必须包含：证据+订单号+处理建议）"},
            {"label": "考核通过标准", "text": "5个模拟case中至少4个处理符合规范\n话术模板能正确使用（不自行创造违规话术）\n知道什么时候该升级，不独自硬扛"},
            {"label": "上岗后支持", "text": "前2周：组长带教，每个case做完后复盘\n第3-4周：独立处理，组长监督\n第5周起：独立上岗，重大case仍需上报"},
            {"label": "持续学习", "text": "每周案例分享会（讨论真实case）\n每月话术库更新（根据新case添加）\n品牌方政策变动时立即同步\n遇到奇葩case立即记录并分享"}
        ]
    }
]

def nl2br(s):
    return s.replace('\n', '<br>')

# Generate scenes HTML
scenes_html = ""
for s in scenes:
    scenes_html += f"""
  <div class="case-card" id="case{s['num']}">
    <div class="case-header">
      <div class="case-num">场景{s['num']}</div>
      <div class="case-title">{s['title']}</div>
      <span class="case-level" style="color:{s['level_color']}; background:{s['level_bg']};">{s['level']}</span>
    </div>
    <div class="case-body">
      <div class="case-summary"><span class="case-tag">📋 场景描述</span><p>{s['summary']}</p></div>
      <div class="case-dialogue"><span class="case-tag">💬 对话还原</span><pre>{s['dialogue'].strip()}</pre></div>
      <div class="case-wrong-box">
        <div class="case-tag-danger">❌ 错误应对（实际发生）</div>
        <div class="script-box danger-script">{s['wrong']}</div>
      </div>
      <div class="case-right-box">
        <div class="case-tag-success">✅ 正确拆解</div>
        <div class="script-box success-script">{nl2br(s['right'])}</div>
      </div>
      <div class="case-lesson-box">
        <div class="case-tag">🎯 核心教训</div>
        <p>{s['lesson']}</p>
      </div>
    </div>
  </div>"""

# Generate training HTML
training_html = ""
for m in training:
    items_html = ""
    for item in m['items']:
        items_html += f'<div class="train-item"><div class="train-label">{item["label"]}</div><div class="train-text">{nl2br(item["text"])}</div></div>'
    training_html += f"""
  <div class="train-card" id="train{m['num']}">
    <div class="train-card-header">
      <div class="train-icon">{m['icon']}</div>
      <div class="train-meta">
        <div class="train-day">第{m['duration']}天</div>
        <div class="train-title">{m['title']}</div>
        <div class="train-subtitle">{m['subtitle']}</div>
      </div>
    </div>
    <div class="train-items">{items_html}</div>
  </div>"""

print(f"Scenes: {len(scenes)}, Training: {len(training)}")

# Find footer
footer_match = re.search(r'<div class="footer">', html)
insert_pos = footer_match.start() if footer_match else html.rfind('</body>')

# Build new sections
scenario_labels = [
    ("场景1", "过期产品要求退款+赔偿", "#C00000"),
    ("场景2", "竞品碰瓷", "#C00000"),
    ("场景3", "拒绝提供证据发帖扩散", "#FF6B00"),
    ("场景4", "开封后退全款", "#FF6B00"),
    ("场景5", "价格下降要求退差价", "#375E10"),
    ("场景6", "一人多号叠加赔偿", "#C00000"),
    ("场景7", "录音留证要求客服出面", "#FF6B00"),
    ("场景8", "直播展示与实物不符", "#C00000"),
    ("场景9", "赠品包装不同", "#375E10"),
    ("场景10", "无证据要求赔偿", "#FF6B00"),
]

scenario_nav_items = "\n".join(
    f'          <a href="#case{i+1}" class="scenario-link" data-case="{i+1}">'
    f'<span class="scenario-dot" style="background:{color}"></span>'
    f'{label} {title}</a>'
    for i, (label, title, color) in enumerate(scenario_labels)
)

new_sections = f'''
  <!-- ==================== SCENARIOS SECTION ==================== -->
  <section class="scenarios-section" id="scenarios">
    <div class="section-header">
      <h2>🧩 售后场景拆解</h2>
      <p>10个真实案例，还原错误vs正确应对方式</p>
    </div>
    <div class="scenarios-grid">
      <div class="scenarios-list">
        <div class="scenario-nav">
          <div class="scenario-nav-title">📂 场景目录</div>
{scenario_nav_items}
        </div>
      </div>
      <div class="scenarios-cases">
        {scenes_html}
      </div>
    </div>
  </section>

  <!-- ==================== TRAINING SECTION ==================== -->
  <section class="training-section" id="training">
    <div class="section-header">
      <h2>📚 新人培训计划</h2>
      <p>5天系统学习，从入门到独立上岗</p>
    </div>
    <div class="training-timeline">
      <div class="training-track">
        <div class="track-line"></div>
        <div class="track-dots">
          <div class="track-dot active" data-day="1">Day 1<br><small>认知<br>入门</small></div>
          <div class="track-dot" data-day="2">Day 2<br><small>情绪<br>流程</small></div>
          <div class="track-dot" data-day="3">Day 3<br><small>客户<br>话术</small></div>
          <div class="track-dot" data-day="4">Day 4<br><small>保护<br>协作</small></div>
          <div class="track-dot" data-day="5">Day 5<br><small>考核<br>上岗</small></div>
        </div>
      </div>
      {training_html}
    </div>
  </section>
'''

new_css = '''
/* ====== SCENARIOS SECTION ====== */
.scenarios-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 60px 24px;
}
.scenarios-grid {
  display: grid;
  grid-template-columns: 220px 1fr;
  gap: 24px;
  align-items: start;
}
.scenarios-list {
  position: sticky;
  top: 90px;
}
.scenario-nav {
  background: #fff;
  border-radius: 16px;
  padding: 20px;
  border: 1px solid #E8F0FE;
  box-shadow: 0 2px 8px rgba(26,54,164,0.06);
}
.scenario-nav-title {
  font-size: 13px;
  font-weight: 700;
  color: #1A36A4;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 12px;
  padding-bottom: 10px;
  border-bottom: 2px solid #E8F0FE;
}
.scenario-link {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 10px;
  border-radius: 8px;
  text-decoration: none;
  color: #444;
  font-size: 13px;
  line-height: 1.4;
  transition: all 0.2s;
}
.scenario-link:hover {
  background: #F0F4FF;
  color: #1A36A4;
}
.scenario-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}
.scenarios-cases {
  display: flex;
  flex-direction: column;
  gap: 24px;
}
.case-card {
  background: #fff;
  border-radius: 16px;
  border: 1px solid #E8F0FE;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(26,54,164,0.06);
  transition: box-shadow 0.2s;
}
.case-card:hover {
  box-shadow: 0 4px 24px rgba(26,54,164,0.12);
}
.case-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 20px;
  background: linear-gradient(135deg, #F8FAFF 0%, #EEF2FF 100%);
  border-bottom: 1px solid #E8F0FE;
}
.case-num {
  background: #1A36A4;
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 20px;
  flex-shrink: 0;
}
.case-title {
  font-size: 15px;
  font-weight: 700;
  color: #1A1A2E;
  flex: 1;
}
.case-level {
  font-size: 11px;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 20px;
  flex-shrink: 0;
}
.case-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.case-tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  font-weight: 700;
  color: #1A36A4;
  background: #EEF2FF;
  padding: 4px 10px;
  border-radius: 6px;
  margin-bottom: 8px;
}
.case-summary p {
  font-size: 14px;
  color: #555;
  line-height: 1.7;
  margin: 0;
}
.case-dialogue pre {
  background: #F8F9FA;
  border: 1px solid #E8E8E8;
  border-radius: 8px;
  padding: 14px 16px;
  font-family: 'Courier New', monospace;
  font-size: 12px;
  line-height: 1.8;
  color: #333;
  white-space: pre-wrap;
  margin: 0;
  border-left: 3px solid #1A36A4;
}
.case-tag-danger {
  font-size: 12px;
  font-weight: 700;
  color: #C00000;
  background: #FFF2F2;
  padding: 4px 10px;
  border-radius: 6px;
  margin-bottom: 8px;
  display: inline-block;
}
.case-tag-success {
  font-size: 12px;
  font-weight: 700;
  color: #375E10;
  background: #EAF2E3;
  padding: 4px 10px;
  border-radius: 6px;
  margin-bottom: 8px;
  display: inline-block;
}
.script-box {
  border-radius: 8px;
  padding: 14px 16px;
  font-size: 13px;
  line-height: 1.7;
}
.danger-script {
  background: #FFF5F5;
  border: 1px solid #FFD0D0;
  color: #8B0000;
}
.success-script {
  background: #F4FAF0;
  border: 1px solid #C8E6B8;
  color: #2D5016;
}
.case-lesson-box p {
  font-size: 14px;
  font-weight: 600;
  color: #1A36A4;
  background: linear-gradient(135deg, #EEF2FF 0%, #F0F4FF 100%);
  padding: 14px 16px;
  border-radius: 10px;
  margin: 0;
  line-height: 1.7;
  border-left: 4px solid #1A36A4;
}

/* ====== TRAINING SECTION ====== */
.training-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 60px 24px;
}
.training-timeline {
  display: flex;
  flex-direction: column;
  gap: 20px;
  position: relative;
}
.training-track {
  position: relative;
  margin-bottom: 20px;
}
.track-line {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #1A36A4 0%, #2B5BE8 50%, #E8F0FE 100%);
  border-radius: 2px;
  transform: translateY(-50%);
}
.track-dots {
  display: flex;
  justify-content: space-between;
  position: relative;
  z-index: 1;
}
.track-dot {
  background: #fff;
  border: 3px solid #1A36A4;
  color: #1A36A4;
  border-radius: 50%;
  width: 64px;
  height: 64px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 800;
  text-align: center;
  line-height: 1.3;
  cursor: pointer;
  transition: all 0.2s;
}
.track-dot.active {
  background: #1A36A4;
  color: #fff;
  box-shadow: 0 0 0 4px rgba(26,54,164,0.2);
}
.track-dot small {
  font-size: 9px;
  font-weight: 600;
  opacity: 0.8;
}
.train-card {
  background: #fff;
  border-radius: 16px;
  border: 1px solid #E8F0FE;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(26,54,164,0.06);
  transition: box-shadow 0.2s;
}
.train-card:hover {
  box-shadow: 0 4px 24px rgba(26,54,164,0.12);
}
.train-card-header {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 18px 20px;
  background: linear-gradient(135deg, #1A36A4 0%, #2B5BE8 100%);
  color: #fff;
}
.train-icon {
  font-size: 32px;
  line-height: 1;
  flex-shrink: 0;
}
.train-meta {
  flex: 1;
}
.train-day {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  opacity: 0.8;
  margin-bottom: 2px;
}
.train-title {
  font-size: 17px;
  font-weight: 800;
  margin-bottom: 2px;
}
.train-subtitle {
  font-size: 12px;
  opacity: 0.85;
}
.train-items {
  padding: 16px 20px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 12px;
}
.train-item {
  background: #F8FAFF;
  border-radius: 10px;
  padding: 14px;
  border: 1px solid #E8F0FE;
}
.train-label {
  font-size: 11px;
  font-weight: 800;
  color: #1A36A4;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 6px;
}
.train-text {
  font-size: 13px;
  color: #444;
  line-height: 1.7;
}

/* ====== RESPONSIVE ====== */
@media (max-width: 768px) {
  .scenarios-grid {
    grid-template-columns: 1fr;
  }
  .scenarios-list {
    position: static;
  }
  .scenario-nav {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4px;
  }
  .scenario-nav-title {
    grid-column: 1 / -1;
  }
  .scenario-link {
    font-size: 12px;
    padding: 6px 8px;
  }
  .train-items {
    grid-template-columns: 1fr;
  }
  .track-dot {
    width: 48px;
    height: 48px;
    font-size: 9px;
  }
  .track-dot small {
    font-size: 8px;
  }
}
'''

# Insert
new_html = html[:insert_pos] + new_sections + html[insert_pos:]
style_close = new_html.rfind('</style>')
new_html = new_html[:style_close] + new_css + new_html[style_close:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Done! Output size: {len(new_html)} chars")
