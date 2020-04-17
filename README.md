# gen_browser_header
gen_browser_header create header for http(s) request, return a **list**    
### install
`pip install gen_browser_header`
### usage
`import gen_browser_header as gbh`    
`import setting`  
`import self.SelfEnum as self_enum`  

`cur_setting = setting.GbhSetting(`)  
`cur_setting.proxy_ip = ['10.11.12.13:8090']`   
`cur_setting.browser_type = {self_enum.BrowserType.Chrome}`  
`cur_setting.firefox_ver = {'min': 74, 'max': 75}`  
`cur_setting.os_type = {self_enum.OsType.Win64}`  
`cur_setting.chrome_type = {self_enum.ChromeType.Stable}`  
`cur_setting.chrome_max_release_year = 1`  

`print(gen_header(setting=cur_setting, num=1))`

### gen_browser_header use gen_header to generate headers, which include 2 parameters: setting and num.  
### setting
gen_browser_header use setting to pass related parameters into function
, setting has below keys:  
1. **proxy_ip**  
type:***list***. For example, [\'10.18.20.71\']  
default: **None**.   
description: When gen_browser_header try to generate
 chrome
 header, it
 need to
 connect to
 https://www.chromedownloads.net/ to get valid chrome version, sometime, can
 't directly connect to it, so need to set proxy ip to connect this url. get
 -browser-header will try each element in **proxy_ip**, until find an valid
  one to use, or can't find any valid, then raise an Exception and exit  
2. **browser_type**  
  type:***set***.  
  default: **self_enum.BrowserType.Firefox**.   
  description: what kind of browser's header to be generated. Currently, only
   support
   firefox
   and chrome. 3 enum value can be choose: self_enum.BrowserType.Chrome
   /self_enum.BrowserType.Firefox/self_enum.BrowserType.All. Notice, if All is
    set
   , Chrome and Firefox will be auto replace All. which means: {self_enum.BrowserType.All} will be convert to
      {self_enum.BrowserType.Chrome
   , self_enum.BrowserType.Firefox} internally  
3. **firefox_ver**  
  type:***dict***.   
  default: **{'min':64, 'max':75}**  
  description: the firefox version range, in which range, a firefox header
   will be
   generate. This parameter is a dict, include 2 keys: min and max, the
    related version info can be found in http://ftp.mozilla.org/pub/firefox
    /releases/. An exampleL {'min': 64, 'max': 75}  
4. **os_type**    
   type:***set***.  
   default: **self_enum.OsType.Win64**.    
   description: In which kind of operation system, the header generated
   . Currently
   , only 3
    enum value can be choose:  self_enum.OsType.Win32/self_enum.OsType.Win64
    /self_enum.OsType.All. Notice, if All is set, Win32 and Win64 will be
     auto replace All. which means: {self_enum.OsType.All} will be convert to
      {self_enum.OsType.Win32, self_enum.OsType.Win64} internally  
5. **chrome_type**    
type:***set***.   
default: **self_enum.ChromeType.Stable**.  
description: chrome has 4 different type: stable/beta/dev/canary, related
 enum value are
 self_enum.ChromeType.Stable
/self_enum.ChromeType.Beta/self_enum.ChromeType.Dev/self_enum.ChromeType
.Canary. An addition enum value self_enum.ChromeType.All also valid, it All
 is set, chrome_type will be replace to include all 4 chrome type internally. which means: {self_enum.ChromeType.All} will be convert to
      {self_enum.ChromeType.Win32, self_enum.OsType.Win64} internally  
6. **chrome_max_release_year**    
type: ***int***.   
default: **1**.  
description: how long ago, chrome version should be choose, the max value is
 `current year - 2008`, 2008 is the year that chrome released
 
 ### num
 type: ***int***.  
 default: **None**. 
 how many header will be generate. if not set(default value is None), all
  generate header will be return, otherwise, the ***num*** headers will be
   return
