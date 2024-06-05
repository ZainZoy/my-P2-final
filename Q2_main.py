from Q2_host import *
from Q2_booking import *
from Q2_user import *
from Q2_guest import *
from Q2_Review import *
host1 = Host("Zain", "7018", "27105", [])
host1.add_property(190,"fc","fccu","uni",1901019)
host1.display_properties()
g1 = Guest("li",909,7777,[])
# g1.book_property(190,10,20)