import pyautogui
import time
from util import *

def main():
	# Создаем список с данными и лист ошибок error_list, в которую будем добавлять данные, которые вызвали ошибку
	lst = ['2', '4', '9', '6']
	error_list = []	
	
	# Задаем количество номеров и создаем счетчики для индексов
	number = 5 
	f = 0
	h = 1

	# Открываем ОСНОВНОЙ цикл и двигаемся ко входу и нажимаем на кнопку входа
	for i in range(number):
		pyautogui.moveTo(135, 105, 2)
		pyautogui.click()
		time.sleep(2)
		
		# В первую и вторую форму вводим данные
		pyautogui.write(lst[f])
		pyautogui.moveTo(1201, 450, 1)
		pyautogui.drag(-110, 0, 2, button='left')
		time.sleep(1)
		pyautogui.write(lst[h])
		f += 2
		h += 2

		# Запускаем
		pyautogui.moveTo(980, 540, 1)
		pyautogui.click()
		
		# Создаем счетчик, который ограничит время ожидания для входа в 4 минуты
		time_enter_limit = 0

		# Ждем пока загрузится страница, пока белый пиксель равен белому или не вышла ошибка, работает цикл
		while pyautogui.pixel(701, 194) == pyautogui.pixel(1415, 780):
			time.sleep(3)
			time_enter_limit += 1
			# Если эти условия наступили, то выходим из этого цикла while	
			if pyautogui.pixel(756, 489) == (130, 138, 123):
				break
			if pyautogui.pixel(462, 134) == (205, 10, 58):
				break		
			if time_enter_limit == 80:
				break
		
		# Условия, при которых выйдем из этой итерации цикла for и начинаем заново следующий цикл,
		# перед этим добавив вызвавшие ошибки данные в лист ошибок
		if time_enter_limit == 80:
			stop_and_quit()
			add_errors_to_list()
			continue
		if pyautogui.pixel(662, 424) == (255, 110, 23):
			pyautogui.moveTo(1439, 504, 1)
			pyautogui.click()
			add_errors_to_list()
			continue
		if pyautogui.pixel(656, 489) == (134, 110, 53):
			pyautogui.moveTo(728, 376, 1)
			pyautogui.click()
			add_errors_to_list()
			continue
		
		time.sleep(1)

		# Создаем счетчик 
		k = 0
		
		# Пока в пикселях будет нужный нам цвет, то будет работать цикл и условия
		while pyautogui.pixel(601, 494) != pyautogui.pixel(1040, 580): 
			if pyautogui.pixelMatchesColor(896, 233, (255, 255, 255)):
				if not pyautogui.pixelMatchesColor(941, 770, (255, 255, 255)):
					if pyautogui.pixelMatchesColor(849, 629, (255, 255, 255)):
						# Все условия выполнены, значит выбираем строку	
						pyautogui.moveTo(35, 524)
						pyautogui.click()
						change_position()
						k += 1
					# Иначе то идем и промотаем эту строчку	
					else:
						change_position()
				if pyautogui.pixelMatchesColor(941, 770, (255, 255, 255)):
					if pyautogui.pixelMatchesColor(855, 587, (255, 255, 255)):
						change_position()
					# Иначе то идем и промотаем эту строчку	
					else:
						change_position()
			# Если в условии нет нужного нам цвета, то мы перемотаем строку
		    else:
		    	change_position()

main()
