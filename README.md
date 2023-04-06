# e-cology9-sql
泛微e-cology9 SQL注入验证脚本
## 说明

本项目功能为QVD-2023-5012-泛微E-cology9 SQL批量验证

## 各文件功能

poc.py为验证脚本

ip.txt放置目标url，需要携带协议头

```
http://127.0.0.1
https://127.0.0.1
```

result.txt为结果输出，存在漏洞的目标将会存放至result.txt

requirements.txt为py所需依赖

url3.py为sqlmap tamper脚本

## 使用说明

```
pip install requitrements.txt
python poc.py
```

```
sqlmap --tamper=url3.py -u "url"
```

