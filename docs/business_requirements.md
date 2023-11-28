# Бизнес-требования

Разрабатываемый проект предназначен для упрощения поиска единомышленников, заинтересованных в реализации различных IT-проектов (далее - Система).

## Действующие лица

С системой взаимодействуют следующие действующие лица:
- "Хабр" - одноименный крупный в рунете веб-сайт, посвященный IT тематике и содержащий различную информацию о своих пользователях;
- Пользователь ХаброЛинкера - в целом любой человек, взаимодействующий с Системой;
- Незарегистрированный пользователь ХаброЛинкера - Пользователь ХаброЛинкера, который не имеет учётную запись в Системе;
- Зарегистрированный пользователь ХаброЛинкера - Пользователь ХаброЛинкера, который имеет учётную запись в Системе.

## Варианты использования

Варианты использования - высокоуровневые сценарии, описывающие задачи, которые выполняет система и действующие лица, которые в этих сценариях участвуют.

**"Хабр"**
- Предоставляет данные о единомышленниках, зарегистрированных на сайте Хабр.

**Пользователь ХаброЛинкера**
- Управление фильтрами поиска (выбор специализации единомышленников, опыта работы и тд) и поиск единомышленников по этим фильтрам.

**Незарегистрированный пользователь ХаброЛинкера**
- Регистрация в Системе.

**Зарегистрированный пользователь ХаброЛинкера**
- Управление данными личного профиля.
- Управление единомышленниками найденных по определенным фильтрам поиска:
  - Сохранение;
  - Просмотр;
  - Удаление.
- Коммуникация с единомышленниками:
    - Получение сообщений;
    - Просмотр диалога;
    - Отправка сообщений.

Диаграмма вариантов использования приведены на следующем рисунке.

![use_case](./use_case.png)