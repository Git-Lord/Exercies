#Цель, имя исполняемого файла
TARGET = helloworld

#Директория для установки приложения
PREFIX = /usr/local/bin

#Существующие исходники
SRCS = main.cpp helloworld.cpp

#Объектные файлы
OBJS = $(SRCS:.cpp=.o)

#Используемый компилятор
CC = g++

#Параметры комплияции
CFLAGS=-c

#Команды, которые не связаны с файлами
.PHONY: all clean install uninstall

#Команда выполняемая по умолчанию
all: $(TARGET)

#Линковка
$(TARGET):  $(OBJS)
			$(CC) $(OBJS) -o $(TARGET)

#Очистка директории
clean:
		rm -rf $(TARGET) $(OBJS)

#Установка
install:
		install $(TARGET) $(PREFIX)

#Удаление
uninstall:
		rm -rf $(PREFIX)/$(TARGET)
