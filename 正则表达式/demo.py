import re
text="""薛：如果说我见你 如果碰巧你会接近
薛：如果说我问你 如果碰巧你会答应
郁：如果这是道双向选择题 如果还有些可能性
薛：那只要我还是我 就无条件相信
合：如果说你看我 如果恰好我也回应
合：如果说你牵我 如果恰好我也握紧
合：如果这时刻仅限于梦境 如果总归都会清醒
合：但只要你还是你 又有什么问题
薛：所以
你还是你吗
郁：我还是我啊
薛：那我可以
合：掺借幽默表达
发个誓约 等三年 六年 十年 算了 要什么期限
郁：那你还是你吗
薛：当然啊
郁：那不如我们
合：就签字画押
是今天下午 还是明天早上

薛：如果说
郁：如果说
薛：如果说
薛：如果说
郁：如果说
薛：所以你还是你吗
郁：我还是我啊
薛：那我可以
合：掺借幽默表达
发个誓约 等三年 六年 十年 算了 要什么期限
郁：那你还是你吗
薛：当然啊
郁：那不如我们
合：就签字画押
就今天下午 还是明天早上
薛：遗憾的是这如果也只是如果
合：如果说这次如果并非如果"""
result=re.finditer(r'：(?P<ccc>.*)',text)
for i in result:
    print(i.group('ccc'))