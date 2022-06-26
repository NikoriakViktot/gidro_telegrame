# -*- coding: utf-8 -*-
import sys, os, shutil, sqlite3
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QApplication, QFileDialog, QPixmap
from SQL_pictures_ui import Ui_MainWindow


def sqlite3_read_pictures_specs_from_db(data_base, table):
    """
    Функция для чтения сведений о рисунках, записаных в указанной таблице (table)
    указанной базы данных (data_base) сведения включают id, описание рисунка, путь из которого рисунок импортирован
    """
    # Соединяемся с базой данных
    con = sqlite3.connect(str(data_base))
    # Создаем объект курсора
    cur = con.cursor()
    try:
        query = 'SELECT id, description, path FROM '+table
        cur.execute(query)
        data = cur.fetchall()
    except sqlite3.OperationalError:
        data = None
    cur.close()
    # Разрываем соединение с базой
    con.close()
    return data


def sqlite3_simple_pict_import(data_base, table, pict_path, record_id, description):
    """
    Функция для создания таблицы в базе данных с использование СУБД sqlite3
    Таблица создается для хранения рисунков в формате BLOB, после
    создания таблицы туда помещается рисунок по пути pict_path
    """
    # Соединяемся с базой данных, если базы данных нет создается новая с таким именем
    con = sqlite3.connect(data_base)
    # Создаем объект курсора
    cur = con.cursor()
    query_creation = 'CREATE TABLE IF NOT EXISTS '+str(table)+' (id TEXT, description TEXT, path TEXT,data BLOB)'
    # Создаем таблицу если таблицы не существует
    cur.execute(query_creation)
    binary_pict = import_pict_binary(pict_path)
    data = (record_id, description, pict_path, binary_pict)
    query = 'INSERT INTO '+table+' VALUES(?, ?, ?, ?)'
    cur.execute(query, data)
    con.commit()
    cur.close()
    con.close()


def export_pict_from_sql(data_base, table, record_id, path):
    """
    Чтение рисунка из таблицы (table) базы данных (data_base) по уникальному идентификатору (id)
    и запись его с тем же именем, что и указано в базе данных, но по новому пути (new_path)
    """
    con = sqlite3.connect(data_base)
    # Создаем объект курсора
    cur = con.cursor()
    query = 'SELECT data, path, description FROM '+table+' WHERE id = "'+record_id+'"'
    cur.execute(query)
    record = cur.fetchone()
    pict_binary = record[0]
    write_pict_from_binary(path, pict_binary)
    return


def sqlite3_simple_delete_record(data_base, table, id_column, record_id):
    """
    Функция для удаления записи в указанной таблице, указанной базы данных
    по названию колонки (id column) и значению ячейки (record_id) в указанной колонке
    """
    # Соединяемся с базой данных
    con = sqlite3.connect(data_base)
    # Создаем объект курсора
    cur = con.cursor()
    # Создаем запрос на удаление записи по ключу record_id из колонки ключей id_column
    query = 'DELETE FROM '+table+' WHERE '+id_column+" = '"+record_id+"'"
    cur.execute(query)
    # Подтверждаем изменения
    con.commit()
    # Закрываем курсор
    cur.close()
    # Разрываем соединение с базой
    con.close()


def import_pict_binary(pict_path):
    f = open(pict_path, 'rb')
    pict_binary = f.read()
    return pict_binary


def write_pict_from_binary(file_path, pict_binary):
    f = open(file_path, 'wb')
    f.write(pict_binary)


def make_dir_if_it_is_not_exists(container_tmp_dir):
    directory = os.getcwd()+'\\tmp'
    if not os.path.exists(directory):
        os.makedirs(directory)
        container_tmp_dir.append(directory)
    return directory


def add_element_to_list_widget(item_name, list_widget, icon):
    item = QtGui.QListWidgetItem()  # Cоздаём объект QListWigetItem
    item.setIcon(QtGui.QIcon(icon))  # Добавляем объект иконки (Qicon) для объекта QListWigetItem
    item.setText(item_name)  # Добавляем название итема
    list_widget.addItem(item)


def adjust_buttons_in_work_with_pictures_main_window(self):
    # Функция для настройки работы кнопок в главном окне программы для работы с рисунками
    self.pushButton_choose_image.clicked.connect(self.choose_picture_dialog_open)
    self.pushButton_by_default.clicked.connect(self.by_default_setup)
    self.pushButton_show_pict_in_data_base.clicked.connect(self.show_images_stored_in_database)
    self.pushButton_load_image.clicked.connect(self.load_image_to_db)
    self.pushButton_export_image.clicked.connect(self.unload_image_from_sql)


class MainWindowWorkWithPictures(QMainWindow, Ui_MainWindow):
    tmp_dirs = []

    def __init__(self):
        QMainWindow.__init__(self)
        # Настройка основного GUI
        self.setupUi(self)

        adjust_buttons_in_work_with_pictures_main_window(self)

    def choose_picture_dialog_open(self):
        fname = QFileDialog.getOpenFileName(self,
                                            'Choose picture',
                                            './')
        self.pict_path_lineEdit.setText(fname)
        pixmap = QPixmap(fname)
        pixmap_resize = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label_for_pic.setPixmap(pixmap_resize)

    def by_default_setup(self):
        self.data_base_lineEdit.setText('.\\test_data\\PictDatabase.db')
        self.table_lineEdit.setText('pictures')
        self.pict_export_lineEdit.setText('.\\test_data\\some_pict.jpg')

    def load_image_to_db(self):
        # Функция для загрузки изображений в базу данных, сведения о базе данных, таблице для загрузке
        # адреса рисунка для загрузки, его уникального идентификатора и описания получаются из соответствующих
        # совместимого графического интерфейса программы
        data_base = self.data_base_lineEdit.text()  # Получаем путь к базе из поля ввода
        table = self.table_lineEdit.text()  # Получаем название таблицы в базе из поля ввода
        record_id = self.id_lineEdit.text()  # Получаем уникалдьный id из поля ввода
        description = self.description_lineEdit.text()  # Получаем описние рисунка из поля ввода
        pict_path = self.pict_path_lineEdit.text()  # Получаем путь к рисунку из поля ввода
        # Запускаем функцию загрузки рисунка передавая туда все необходимые сведения
        sqlite3_simple_pict_import(data_base, table, pict_path, record_id, description)

    def show_images_stored_in_database(self):
        # Функция для отображения рисунков в списке
        # совместимого графического интерфейса программы, принимает на вход путь к базе данных
        data_base = self.data_base_lineEdit.text()  # Получаем путь к базе из поля ввода
        table = self.table_lineEdit.text()  # Получаем название таблицы в базе из поля ввода
        # Для получения данных о спецификации рисунков (не самих рисунков, а: id, description, path)
        # применяем соответствующую функцию c указанием базы данных(пути к базе) и таблицы в этой базе
        data = sqlite3_read_pictures_specs_from_db(data_base, table)
        # В случае если таблицы несуществует, либо если по какой либо другой причине возникает ошибка
        # то data присваивается значение None
        if data is None:  # В этом случае выводим в текстовое поле, что в такой-то таблице нет данных
            self.textBrowser_for_statistics.setText('There is no data in '+data_base+' table ' + table)
        else:  # Иначе перебираем спецификации отдельных рисунков создаем для них временный путь
            # Но в начале в базовом каталоге программы создаем папку tmp
            tmp_directory = make_dir_if_it_is_not_exists(self.tmp_dirs)
            self.listWidget_images.clear()
            for pict_specs in data:  # Перебираем спецификации рисунков
                # Получаем расширение рисунка из старого пути колонка 3 базы данных
                extension = pict_specs[2][pict_specs[2].rfind('.'):len(pict_specs[2])]
                # Создаем временный путь к файлу
                temporary_path = tmp_directory + '\\tmp'+extension
                i = 0  # Устанавливаем счетчик на 0
                # В случае если такой временный файл уже есть прибавляем к счетчику 1 и повторяем пока уникальный
                # путь не будет получен
                while (os.path.exists(temporary_path)) is True:
                    i = i+1
                    temporary_path = tmp_directory+'\\'+'tmp'+str(i)+extension
                # Экспортируем рисунок по временному пути
                export_pict_from_sql(data_base, table, pict_specs[0], temporary_path)
                # Создаем элемент QListWidgetItem и добавляем его в список
                add_element_to_list_widget('#'+str(pict_specs[0])+'. '+str(pict_specs[1]), self.listWidget_images, temporary_path)
            # Выводим в текстовое поле надпись
            self.textBrowser_for_statistics.setText('pictures in '+data_base+' table '
                                                    + table + ' are shown in list at the left')

    def unload_image_from_sql(self):
        selected_item = self.listWidget_images.currentRow()
        data_base = self.data_base_lineEdit.text()  # Получаем путь к базе из поля ввода
        table = self.table_lineEdit.text()  # Получаем название таблицы в базе из поля ввода
        path = self.pict_export_lineEdit.text()  # Получаем путь к рисунку из текстого поля

        data = sqlite3_read_pictures_specs_from_db(data_base, table)

        try:
            record_id = data[selected_item][0]
            old_path = data[selected_item][2]
            extension = old_path[old_path.rfind('.'):len(old_path)]
            path = path[:path.rfind('.')]+extension
            export_pict_from_sql(data_base, table, record_id, path)
            self.textBrowser_for_statistics.setText('image with record id=' + str(record_id) + ' successfuly unloaded')
        except:
            self.textBrowser_for_statistics.setText('В процессе экспорта рисунка произошла какая-то ошибка')

def main_application_sql():
    """
    Функция для инициализации и отображения основного окна приложения для работы с рисунками
    """
    # Класс QApplication руководит управляющей логикой ГПИ и основными настройками.
    # Здеь мы создаем экземпляр класса QAplication передавая ему аргументы из коммандной строки.
    app = QApplication(sys.argv)  # где sys.argv список аргументов командной строки, передаваемых сценарию Python.
    app.setStyle('cleanlooks')
    # Здсь мы создаем экземпляр класса MainWindow.
    main = MainWindowWorkWithPictures()
    main.show()
    # Метод show() отображает виджет на экране.Виджет сначала создаётся в памяти, и
    # только потом(с помощью метода show) показывается на экране.

    # Теперь ловим статус выхода из программы
    status = app.exec_()

    # После выхода из программы удаляем временный каталог
    for dir in main.tmp_dirs:
        shutil.rmtree(dir)

    # После подчистки всех хвостов делаем чистый выход
    sys.exit(status)

    # exec_ запускает цикл обработки сообщений
    # и ждет, пока не будет вызвана exit() или не
    # будет разрушен главный виджет, и возвращает значение установленное в exit().
    # Здесь sys.exit обеспечивает чистый выход из приложения.


if __name__ == '__main__':
    main_application_sql()

