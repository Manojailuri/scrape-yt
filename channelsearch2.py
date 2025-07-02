from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import datetime
xdt = datetime.datetime.now()
print("Where do you want to search?\n 1. Channel\n 2. Home page\n 3. Search results \n 4. Recent uploads of selected channels")
doo = int(input("Enter your choice: "))

print("list to be sorted based on: \n 1) Likes \n 2) Views \n 3) likes:views ratio \n 4) Comments")
valu = int(input("Choose a value: "))
with open('selectors.txt', 'r', encoding='utf-8') as file:
	selectors = file.readlines()

def sortway(views, likes, addrr, value, comments):

	match value:
		case 1:
			return [likes, views, addrr]
		case 2:
			return [views, likes, addrr]
		case 3:
			try:
				return [likes/views, views, likes, addrr]
			except:
				return [0, 0, 0, 0]
		case 4:
			return [comments, views, likes, addrr]



class ytrecompile:
	# Number of elements unavailable increments by 1 if the element not found
	unavailable = 0
	# Wait time
	waitt = 5
	
	# Function to use if a driver variable is set to a web browser
	def getaddr(self, vale, driv):
		# Scroll down
		ActionChains(driv)\
			.key_down(Keys.PAGE_DOWN)\
			.perform()
		
		# Wait
		driver.implicitly_wait(5)
		
		# Find the element and store the address of it in "addr"
		try:
			elem = driv.find_element(By.CSS_SELECTOR, vale)
			addr = elem.get_attribute("href")
		except:
			print("The element not found")
			self.unavailable += 1
			return "FNF"
			
		return addr
		
	def vidvals(self, addre, driv):
		views = ""
		likes = ""
		comments = ""
		cms = 0
		try:
			driv.get(addre)
			driv.implicitly_wait(5)
			#views = driv.find_element(By.CSS_SELECTOR, '#description-inner > div:nth-child(1) > yt-formatted-string:nth-child(1) > span:nth-child(1)')
			#print(selectors[3])
			views = driv.find_element(By.CSS_SELECTOR, selectors[3])
			likes = driv.find_element(By.CSS_SELECTOR, selectors[5])
			
			if valu == 4:
				try:
					comments = driv.find_element(By.CSS_SELECTOR, '.count-text > span:nth-child(1)')
					cms = 1
				except:
					cms = 0
		except:
			self.unavailable += 1
			return ["FNF", "FNF", "FNF"]
		#title = ""
		#channel = ""
		#subs = ""
		#disc = ""
		#rdate = ""
		
		if cms != 0:
			cms = comments.text

		valarr = [views.text, likes.text, cms]
		#print(valarr)
		return valarr
		
	def formatting(self, views, likes, comments):
		#Views
		outview = 0
		separ = views.split(" ")
		if views == "FNF" or likes == "FNF":
			return ["FNF", "FNF", "FNF"]
		def multip(x):
			if x == 'M':
				return 1000000
			elif x == 'K':
				return 1000
			elif x == 'B':
				return 1000000000
			else:
				return 1
		if separ[0][-1].isalpha():
			numview = ''.join(separ[0][:(len(separ[0])-1)])
			#print(numview)
			outview = float(numview) * multip(separ[0][-1])
			#print(outview)
			#print(numview)
		elif ',' in separ[0]:
			outview = int(''.join(separ[0].split(",")))
			#print(outview)
			#print(separ[0])
		else:
			outview = float(separ[0])
			#print(outview)
			#print(separ[0])
			
		#Likes
		outlike = 0
		if likes[-1].isalpha():
			numview = ''.join(likes[:(len(likes)-1)])
			if numview != 'Lik':
				try:
					outlike = float(numview) * multip(likes[-1])
				except:
					outlike = 0
			else:
				outlike = 1
			#print(outlike)
		else:
			try:
				outlike = float(likes)
			#print(outlike)
			except:
				outlike = 0
		
		if comments != 0:
			comments = comments.split(",")
			comments = ''.join(comments)
	
		comments = int(comments)
			
		forarr = [outview, outlike, comments]
		return forarr
		
		

match doo:
	case 1:
		number = 0
		varr = int(input("Enter the number of rows to calc: "))
		handle = input("Enter the channel handle: ")
		filee = open( handle + ".txt", "a")
		filee.write("\n")
		filee.write(str(xdt) + "\n")
		driver = webdriver.Firefox()
		#driver.minimize_window()
		
		driver.get('https://www.youtube.com/@' + handle + '/videos')
		sel = selectors[1]
		
		#elem = driver.find_element(By.CSS_SELECTOR, sel)

		addrs = []
		arr = []
		vids = ytrecompile()

		for i in range(varr):
			for j in range(4):
				if vids.unavailable > 20:
					break
				value = sel[:40] + str(i + 1) + sel[41:97] + str(j + 1) + sel[98:]
				#print(value)
				addr = vids.getaddr(value, driver)
				if addr != "FNF":
					addrs.append(addr)

		print(len(addrs))
		driver.quit()
		drivs = []
		for g in range(len(addrs)):
			print(addrs[g])

		valll = ytrecompile()
		def opendrivs(nnn):
			for n in range(nnn):
				drivs.append(webdriver.Firefox())
		def quitdrivs(nnn):
			for j in range(nnn):
				drivs[j].quit()
		#opendrivs(5)
		webi = 0
		drivv = webdriver.Firefox()
		for k in range(len(addrs)):
			webi += 1
			if webi > 60:
				drivv.quit()
				drivv = webdriver.Firefox()
				webi = 0
			#drivs[k%5] = webdriver.Firefox()
			uvals = valll.vidvals(addrs[k], drivv)
			#drivs[k%5].quit()
			#print(uvals)
			fvals = valll.formatting(uvals[0], uvals[1], uvals[2])
			print(fvals)
			print(str(k) + "/" + str(len(addrs)))
			if fvals[0] != "FNF" or fvals[1] != "FNF" or fvals[2] != "FNF":
				arr.append(sortway(fvals[0], fvals[1], addrs[k], valu, fvals[2]))
				#arr.append([fvals[1], fvals[0], addrs[k]])
			#if k%5 == 0:
			#	quitdrivs(5)


		drivv.quit()
		#quitdrivs(5)
		print(len(arr))	
		arr.sort()	
		for j in range(len(arr)):
			print(arr[j])	
			filee.write(str(arr[j]) + "\n")
				
	case 2:
		
		number = 0
		varr = int(input("Enter the number of rows to calc: "))	
		filee = open("sortedhomeyt.txt", "a")
		filee.write("\n")
		filee.write(str(xdt) + "\n")
		driver = webdriver.Firefox()
		driver.get('https://www.youtube.com')
		sel = 'ytd-rich-grid-row.style-scope:nth-child(2) > div:nth-child(1) > ytd-rich-item-renderer:nth-child(1) > div:nth-child(1) > ytd-rich-grid-media:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(2)'
		addrs = []
		arr = []
		vids = ytrecompile()
		for i in range(varr):
			for j in range(3):
				if vids.unavailable > 20:
					break
				value = sel[:40] + str(i + 1) + sel[41:97] + str(j + 1) + sel[98:]
				#print(value)
				addr = vids.getaddr(value, driver)
				if addr != "FNF":
					addrs.append(addr)

		print(len(addrs))
		driver.quit()
		drivs = []
		for g in range(len(addrs)):
			print(addrs[g])

		valll = ytrecompile()
		
		#opendrivs(5)
		webi = 0
		drivv = webdriver.Firefox()
		for k in range(len(addrs)):
			webi += 1
			if webi > 60:
				drivv.quit()
				drivv = webdriver.Firefox()
				webi = 0
			#drivs[k%5] = webdriver.Firefox()
			uvals = valll.vidvals(addrs[k], drivv)
			#drivs[k%5].quit()
			#print(uvals)
			fvals = valll.formatting(uvals[0], uvals[1], uvals[2])
			print(fvals)
			print(str(k) + "/" + str(len(addrs)))
			if fvals != ["FNF", "FNF"]:
				arr.append(sortway(fvals[0], fvals[1], addrs[k], valu, fvals[2]))
				#arr.append([fvals[1], fvals[0], addrs[k]])
			#if k%5 == 0:
			#	quitdrivs(5)


		drivv.quit()
		#quitdrivs(5)
		print(len(arr))	
		arr.sort()	
		for j in range(len(arr)):
			print(arr[j])	
			filee.write(str(arr[j]) + "\n")
		
	case 3:
		filee = open("searchres.txt", "a")
		varr = int(input("Enter the number of rows to calc: "))
		query = input("Enter the search query: ")
		filee.write("\n")
		filee.write("Query =" + query + "\n")
		filee.write(str(xdt) + "\n")
		driver = webdriver.Firefox()
		#driver.minimize_window()
		squery = 'https://www.youtube.com/results?search_query=' + query
		driver.get(squery)
		sel = 'ytd-video-renderer.style-scope:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(2)'
		sel1 = 'ytd-item-section-renderer.style-scope:nth-child(2) > div:nth-child(3) > ytd-video-renderer:nth-child(18) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(2)'
		

		addrs = []
		arr = []
		vids = ytrecompile()
		"""for i in range(varr):
			value = sel[:41] + str(i + 1) + sel[42:]
			addr = vids.getaddr(value, driver)
			if addr != "FNF":
				addrs.append(addr)"""

		for u in range(int(varr/10)):
			for o in range(10):
				value = sel1[:48] + str(u + 1) + sel1[49:101] + str(o + 1) + sel1[103:]
				addr = vids.getaddr(value, driver)
				if addr != "FNF":
					addrs.append(addr)


		driver.quit()
		vids = ytrecompile()
		for g in range(len(addrs)):
			print(addrs[g])

		valll = ytrecompile()
		
		#opendrivs(5)
		webi = 0
		drivv = webdriver.Firefox()
		for k in range(len(addrs)):
			webi += 1
			if webi > 60:
				drivv.quit()
				drivv = webdriver.Firefox()
				webi = 0
			#drivs[k%5] = webdriver.Firefox()
			uvals = valll.vidvals(addrs[k], drivv)
			#drivs[k%5].quit()
			#print(uvals)
			fvals = valll.formatting(uvals[0], uvals[1], uvals[2])
			print(fvals)
			print(str(k) + "/" + str(len(addrs)))
			if fvals != ["FNF", "FNF"]:
				arr.append(sortway(fvals[0], fvals[1], addrs[k], valu, fvals[2]))
				#arr.append([fvals[1], fvals[0], addrs[k]])


		drivv.quit()
		#quitdrivs(5)
		print(len(arr))	
		arr.sort()	
		for j in range(len(arr)):
			print(arr[j])	
			filee.write(str(arr[j]) + "\n")
			
	
	case 4:
		driver = webdriver.Firefox()
		driver.minimize_window()

		channels = ['sochbymm',
		 'MichaelReeves',
		 'DailyDoseOfInternet',
		 'dhruvrathee',
		 'NOTYOURTYPE',
		 'mkbhd',
		 'LazarBeam',
		 'theodd1sout', 
		 'IceCreamSandwich', 
		  ]

		print(channels)
		val = ""
		for i in channels:
			val = "https://www.youtube.com/@" + i + "/videos"
			driver.get(val)
			driver.implicitly_wait(15)
			elem1 = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[2]/div[1]/ytd-video-meta-block/div[1]/div[2]/span[2]").text
	
			words = elem1.split(" ");
	
			if (words[1] == "day" or words[1] == "hours"):
				print(elem1)
				print(i)	

		driver.quit()

			
			
			
