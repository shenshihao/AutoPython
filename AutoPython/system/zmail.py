import poplib
email='1546126430@qq.com'
password='rxooqtesnrqtihhi'
server=poplib.POP3_SSL('mail.qq.com')
print(server)
server.user(email)
server.pass_(password)
resp, mails, octets = server.list()
index = len(mails)#邮件的总数
print(index)
#server.dele(index) 删除邮件 dele可以用于删除制定位置的邮件
resp, lines, octets = server.retr(index)#可以取出最新的邮件的信息