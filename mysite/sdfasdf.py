class last_calls_to_calendar(models.AbstractModel):
	_name="last_calls_to_calendar"

# перед этим добавить 1 поле в настройки компании SOIM PLUS, название поле совпадает с названием функции
#
# 		НАЗВАНИЕ ПОЛЯ: dtct_tg_last_calls_task1 ← цифра в конце может быть от 1 до 24, так было задуманно
# 		ЗНАЧЕНИЕ ПОЛЯ: {cm, 2020, 01}{ultimul apel [date] verificati daca totul este bine}{ AnaStasia, caterina, Pav,Sil,Vla }{3, 0, 1,1,-1}
#
#		разделитель является знаки {}, так как в этом поле 4 настройки:
#
#				a) cm, 2020, 01 ←	 	поле для указания типов контрагентов, разделитель является знак "," запятая, ищет контрагентов
#										по условию "И" (найди компанию у которой тип И cm И 2020 И 01)
#										(в поле можно писать все что угодно, если ничего не найдет, запрос на сервер не улетит,
#										можно ставить неограниченое колличество пробелов, а так же писать большими или маленкими буквами
#
#				b) ultimul apel [date] verificati daca totul este bine ←	текст самого задания который попадет в календарь в ячейку задания,
#																			если в поле присутствует значение [date] дата последнего звонка
#																			будет вставленна вместо [date]
#
#				c) AnaStasia,caterina, Pav, Sil, Vla ←	перечисление пользователей ODOO которым будет равномерно распределено задание, разделитель
#														запятая (в поле нужно вписать пользователей, можно писать и большие	и маленкими буквами, или
#														часть имени, ГЛАВНОЕ чтобы это имя БЫЛО в списке пользователей, иначе пользователь не будет учтён)
#
#				d) 3, 0, 1,1,-1 ←	указываем число заданий которые необходимо распределить в день между пользователями, минусовое значение, означает
#									все остальные ,разделитель является запятой, ОБЯЗАТЕЛЬНО 5 ЗНАЧЕНИЙ, первое значение это значение для понедельника,
#									последнее для пятницы (в поле указать только цифры, если день выполнения кода Cron ODOO	будет средой, то задания
#									появятся на четверг и далее по круго до тех пор пока задания не закончатся ЛИБО не встретит значение минусовое в поле)
#
# а так же в Настройках --> Автоматизация --> Запланированные действия --> добавить запись для запуска этой функции. Указать сегодняшнюю дату, 20 часов(у сервера время по гринвичу, то есть -2 часа от нашего времени), выбрать промежуток времени повторения, колличество запусков -1(для неограниченного колличества)
# пример задания: 	Модель --> 	last_calls_to_calendar
# 				Действие для выполнения --> Выполнить команду на Python
#				Код на Python --> model.dtct_tg_last_calls_task1()




	@api.model
	def dtct_tg_last_calls_task1(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task1')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task2(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task2')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task3(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task3')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task4(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task4')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task5(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task5')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task6(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task6')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task7(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task7')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task8(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task8')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task9(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task9')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task10(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task10')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task11(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task11')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task12(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task12')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task13(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task13')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task14(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task14')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task15(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task15')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task16(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task16')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task17(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task17')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task18(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task18')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task19(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task19')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task20(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task20')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task21(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task21')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task22(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task22')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task23(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task23')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	@api.model
	def dtct_tg_last_calls_task24(self):
		custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task24')
		self.env['last_calls_to_calendar'].last_cals_to_calendar(custom_settings)

	def last_cals_to_calendar(self, custom_settings):
		# custom_settings = self.env['dtct_custom_settings'].get_setting_value('dtct_tg_last_calls_task1')	# получим из настроек компании строку настроек
		from datetime import timedelta

# список custom_settings является набором настроек
		parsed = [str(x.strip('{')).strip() for x in custom_settings.split('}') if str(x.strip('{')).strip()]	# разделим строку на список, разделители {}, уберем пробелы и пустые значения
		types = [x.strip() for x in parsed[0].split(',')]						# типы контрагентов
		text = [x for x in parsed[1].split('[date]')]							# необходимый текст для задания - будер передан в ячейку task
		users = [x.strip() for x in parsed[2].split(',')]						# пользователи ODOO которым необходимо распределить задачи в календаре
		nb_per_day = [int(x.strip()) for x in parsed[3].split(',')]				# на какие дни недели распределить задачи пользователям (количество значеий), и какое колличество задач (значения)

# наполним запрос для пойска
		pers_list = False
		if nb_per_day.count(0) < 5 and len(nb_per_day) == 5:
			date_from=dtct_core.year_end(datetime.today())									# спросим дату окончания года
			date_start=dtct_core.day_end(date_from)-dtct_core.timedelta(days=730)			# выберем дату на 2 года раньше окончания нынешнего года
			search_field = [('chose_type','ilike', types[i]) for i in range(len(types))]	# заполним строку для запроса указаными в настройках типами
			pers_list = self.env['dtct_tg_counterparty_m'].search(search_field)				# найдем контрагентов по типу

# если есть такие компании а так же в днях нет нулей, и есть 5 значений
		if pers_list:
# соединимся с телефонным сервером и поищем последний звонок каждой компании
			mysql_con = pymysql.connect(user = 'officeuser', password = 'update1c', host = '192.168.0.251', database = "asteriskcdrdb")#,database='employees'
			cursor = mysql_con.cursor(pymysql.cursors.DictCursor)

			sql_text=""
			phones = []
			for i,pers in enumerate(pers_list,1):
				phones=pers.get_phones_as_list() 								# найдем все номера телефонов связаные с контрагентом
				sql_text=sql_text+"""
				select max(dates.date) as date_last_call,{id} as counterparty, {cod_fisc} as cf
				from(
				select left(calldate,16) as date, src as phone
				from asteriskcdrdb.cdr
				where lastapp='Dial' and disposition in ('ANSWERED','NO ANSWER') and calldate>='{start_date}' and calldate<='{end_date}' and '{phones}' like concat('%',src,'%')
				)as dates
				""".format(start_date=date_start,end_date=date_from,phones=phones,id=pers.id,cod_fisc=pers.cod_fisc)
				if i!=len(pers_list):
					sql_text=sql_text+"union"
			cursor.execute("select * from("+sql_text+")as sq where sq.date_last_call>'2000-01-01'")
			calls_table = cursor.fetchall()

# превратим данные в список словарей
			list_of_dicts = []
			for el in calls_table:
				list_of_dicts.append({'date_last_call': el.get('date_last_call'), 'counterparty': el.get('counterparty'), 'cf': el.get('cf')})

# найдем id пользователей ODOO по имени или части имени
			users_obj = [self.env['res.users'].search([('name', 'ilike', el)], limit=1) for el in users]
			users_ids = [el.id for el in users_obj if el]

# вычислим дату следующего рабочего дня (функция принимает любую дату, и возвращает дату сл. раб. дня)
			def working_date_after(some_date):
				days_to_next_working_day = 1
				if some_date.weekday() > 3:
					days_to_next_working_day = 7 - some_date.weekday()
				return some_date + timedelta(days=days_to_next_working_day)

# напишем текст с датой
			def task_text(date):
				if len(text) > 1:
					final_text = text[0]
					for i in range(1, len(text)):
						final_text = final_text + date + text[i]
					return final_text
				else: return text[0]

# функция делающая запись в календарь, возвращает значение на 1 больше к task_count
			def create_calendar_vals(day, user_nb, task_count):
				vals = {'day' : str(day)[:10] + ' 08:00:00',
						'asigned_to': users_ids[user_nb%len(users_ids)],
						'counterparty' : list_of_dicts[task_count].get('counterparty'),
						'task' : task_text(list_of_dicts[task_count].get('date_last_call'))}
				self.env['dtct_tg_kme_calendar'].create(vals)
				task_count += 1
				return(task_count)

# закидаем данных в календариссимо
			vals = {}
			task_count = 0
			u_id = 0
			next_working_date = working_date_after(datetime.now())

			while task_count < len(list_of_dicts):
				while nb_per_day[next_working_date.weekday()] == 0: 			# если колличество задач 0 --> найдем следующий рабочий день и посмотрим колличество задач на этот день недели
					next_working_date = working_date_after(next_working_date)
				if nb_per_day[next_working_date.weekday()] > 0:					# если колличество задач в день больше 0 --> распределяем задачи равномерно на пользователей
					for j in range(nb_per_day[next_working_date.weekday()]):
						if task_count < len(list_of_dicts):
							task_count = create_calendar_vals(next_working_date, j, task_count)
						else:
							break
					next_working_date = working_date_after(next_working_date)	# найдем следующий рабочий день
				if nb_per_day[next_working_date.weekday()] < 0:					# если колличество задач меньше 0 --> распределим оставшиеся задачи равномерно на пользователей
					task_count = create_calendar_vals(next_working_date, u_id, task_count)
					u_id += 1


class MyObj(models.Model):
    cashamasha = fieldstype.datetime()




my_dict = [
    {'name': 'John', 'number': '069702468', 'sex' : 'M'},
    {'name': 'Maria', 'number': '025465883', 'sex' : 'F'},
    {'name': 'Grisha', 'number': '069702468', 'sex' : 'M'},
]

@api.model
class Test(models.Model):
    name = fields.Charfield()
    age = fields.Integer()

# pasldkfj = Test(name = "", age = "")
Test.create(name = "", age = "22")
Test.create(name ="", age = "21")




class SomeClass(object):
    attr1 = 42

    def method1(self, x):
        return 2*x

obj = SomeClass()
obj.method1(6) # 12
obj.attr1 # 42

obj1 = SomeClass()
obj1.method1(8) # 12
obj1.attr1 # 42