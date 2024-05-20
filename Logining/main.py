from root import root
from login_page import *

#Login Page Packing
login_entry.grid(column=1, row=0, sticky='w')
login_label.grid(column=0, row=0, sticky='w')
password_entry.grid(column=1, row=1, sticky='w')
password_label.grid(column=0, row=1, sticky='w')
accept_btn.grid(columnspan=2)
accept_btn.grid(column=0, row=2)

root.mainloop()
