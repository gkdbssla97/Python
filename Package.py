# import travel.thailand # 모듈, 패키지만 가능
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

from travel.thailand import *
trip_to = ThailandPackage()
trip_to.detail()

from travel.vietnam import *
trip_to = VietnamPackage()
trip_to.detail()

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()