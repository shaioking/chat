#import re
#n = '丁 Mitzi'
#M = re.sub('\s', '', n)
#M = str(M)

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding= 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None
	丁_word_count = 0
	周_word_count = 0
	丁_sticker_count = 0
	周_sticker_count = 0
	丁_photo_count = 0
	周_photo_count = 0

	#n = '丁 Mitzi'	
	#M = re.sub('\s', '', n)
	#print(M)

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		#print(M)
		if name == '丁':
			if s[3] == '貼圖':
				丁_sticker_count += 1
			elif s[3] == '圖片':
				丁_photo_count += 1
			else:
				for message in s[3:]:
					丁_word_count += len(message)


		elif name == '周校永':
			if s[2] == '貼圖':
				周_sticker_count += 1
			elif s[2] == '圖片':
				周_photo_count += 1
			else:
				for message in s[2:]:
					周_word_count += len(message)

	print('丁說了', 丁_word_count, '個字')
	print('丁傳了', 丁_sticker_count, '個貼圖')
	print('丁傳了', 丁_photo_count, '張圖片')
	print('周說了', 周_word_count, '個字')
	print('周傳了', 周_sticker_count, '個貼圖') 
	print('周傳了', 周_photo_count, '張圖片')

		#print(s)


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('[LINE]丁 Mitzi.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)


main()