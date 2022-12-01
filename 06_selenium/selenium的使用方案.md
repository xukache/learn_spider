总结，selenium的使用方案一般是：
1. 涉及登录，验证码不想搞
<br>可以考虑用selenium完成登录，然后提取cookie，最后用requests发送真正的请求
2. 涉及频繁的校验验证（例如boss）
<br>直接用selenium提取页面源代码，交给lxml处理
