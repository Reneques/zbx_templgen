# zbx_templgen

Скрипт генерирует шаблон zabbix в формате .xml из информации, собранной в YAML 
словаре. Для успешной работы в словарь на основе 2 примеров требуется внести
следущую информацию:

**host**: Общая  информация шаблона
- **group**: Группа для шаблона, в которой он будет состоять
- **template**: Техническое имя шаблона 
- **name**: Визуальное имя шаблона

**applications**: список групп элементов данных

**items**: список словарей с элементами данных: 
- **name**: Имя элемента данных
- **item_type**: Тип элемента данных (SIMPLE/SNMP_AGENT/CALCULATED)
- **application**: Группа элементов данных
- **key**: Ключ (в случае с SIMPLE - выражение, SNMP_AGENT - имя OID,
 CALCULATED - свободное название элемента данных)
- **oid**: (опционально) SNMP OID (если это порт, то OID без концевика порта)
- **delay**: Частота опроса
- **history**: Хранение данных "as is"
- **trends**: Хранение усредненных значений
- **units**: (опционально) Единица измерения
- **param**: (опционально) Выражение вычисляемого элемента данных
- **interfaces**: (опционально) указать словарь интерфейсов для повторения
    данного элемента данных к списку портов
- **triggers**: (опционально, если элементу нужен триггер)
    - **expression**: Выражение триггера
    - **recovery_expression**: (опционально) Выражение закрытия проблемы
    - **name**: Имя триггера
    - **priority**: Важность
    - **manual_close**:(опционально) Опция ручного закрытия (YES)

**graphs**: список словарей с графиками:
- **name**: Имя графика
- **ymin**: (опционально) минимальное значение на графике
- **ymax**: (опционально) максимальное значение на графике
- **g_items**: список словарей с элементами данных в графике
    - **sort**: номер по порядку
    - **drawtype**: (опционально) тип линии (стандартно полоса, можно использовать 
      GRADIENT_LINE/FILLED_REGION/BOLD_LINEDOTTED_LINE/DASHED_LINE
    - **color**: HTML цвет
    - **key**: ключ отображаемого айтема (key)

**ports**: словари с названиями и концевиками oid портов оборудования
- **ports_%value%**:
    - **Gigabit Ethernet 1/0/1**: .1
    - **Gigabit Ethernet 1/0/2**: .2
    
Важны ключи и значения словаря. Элементы данных которые будут ссылаться
на порты будут менять свое имя в таком виде:

`"Item test" >>> "[Gigabit Ethernet 1/0/1]: Item test"`

А OID и ключ будут дописывать концевик в виде:

`ltp8xPONChannelONTCount >>> ltp8xPONChannelONTCount.3`
`1.3.6.1.4.1.35265.1 >>> 1.3.6.1.4.1.35265.1.3`

Также ОЧЕНЬ важно чтобы имена портов совпадали с именами группы элементов
данных по данному порту

#### Применение скрипта:

- В generator.py в блок `if __name__ == '__main__':`
вставить данные с .yml файлом и запустить скрипт. Скрипт вернет строку.
- Если нужен файл - можно запустить вывод в файл командой `python3 generator.py >> ltp8x.xml`
- Можно передать аргументом файл словаря в виде `data/%vendor%/%filename%`

Автор не имеет опыта в создании скриптов, поэтому готов к критике и исправлениям :) 
Также буду стараться дополнять yml файлы для оборудования и буду рад добавить что то по Вашему запросу.  TG: @reneques 

**Огромное спасибо Наташе Самойленко (https://github.com/pyneng) за помощь и курсы!!!**