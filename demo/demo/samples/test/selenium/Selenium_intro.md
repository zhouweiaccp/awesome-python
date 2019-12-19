selenium是一个用于web应用程序测试的工具，selenium测试直接运行在浏览器中，模仿用户操作，支持的浏览器包括IE（7,8,9,10,11），Mozilla Firefox，Safari，Google Chrome，Opera等；

优势
通过编写模仿用户操作的 Selenium测试脚本，可以从终端用户的角度来测试应用程序。
通过在不同浏览器中运行测试，更容易发现浏览器的不兼容性。
支持多平台-windows、linux、MAC
可以把测试用例分布到不同的测试机器上执行、相当于分发机的功能
支持多语言-java、ruby、python、c#
免费开源，对商业用户也没有任何限制
组件
Selenium IDE:一个Firefox插件，可以录制用户的基本操作，生成测试用例。
Selenium Remote Control (RC) :支持多种平台(Windows，Linux，Solaris)和多种浏览器(IE，Firefox，Opera，Safari)，可以用多种语言(Java，Ruby，Python，Perl，PHP，C#)编写测试用例。
Selenium Grid :允许Selenium-RC 针对规模庞大的测试案例集或者需要在不同环境中运行的测试案例集进行扩展。
区别
selenium2
1.Selenium2.0集成了RC和webdriver来提供web UI级自动化测试能力。

2.selenium2.0默认支持firefox浏览器，还是比较方便的，但是selenium2.0对firefox浏览器支持最高只支持46及以下版本，

selenium3
1.selenium 3.0有了更新的特性加入，尤其是对Edge和safari原生驱动的支持，Edge驱动由MS提供，safari原生驱动由Apple提供。

2.在最新的Firefox方面，开始支持Mlzilla的geckodriver驱动，来驱动Firefox的控制。

3.selenium3.0可以支持firefox47以上版本，但是许要下载geckodriver.exe驱动，并添加到环境变量path下

作者：草虫1984
链接：https://www.jianshu.com/p/ca97c8fa3f21
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。