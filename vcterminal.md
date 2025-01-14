git config --list
Настройка пользователя:
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

staging area: 
    область подготовки, индекс, контейнер, хранит текущее состояние изменений перед их фиксацией в репозитории,
Untracked: 
    новый или «git restore --staged <файл>...» убрали из индекса, неотслеживаемый, файл не отслеживается, Git не знает о его существовании. Он есть в рабочем каталоге (когда вы работаете в нём), но не включён в область подготовки и не добавлен в Git,
unmodified: 
    неизменный, файл не менялся с момента последнего коммита. Git следит за ним, его содержимое не изменено,
Modified: 
    Изменения, которые не в индексе для коммита, изменённый файл менялся с момента последнего коммита. Git заметил изменения в нём, но пока включен в следующий коммит. Файл находится в рабочем каталоге, но не добавлен в область подготовки, чтобы быть включённым в следующий коммит,
stAged: 
    git add -A, отслеживаемый, изменённый файл, который добавлен в область подготовки и готов к включению в следующий коммит. Git готов сохранить его состояние в репозитории, (используйте «git restore --staged <файл>...», чтобы убрать из индекса). Команда git add -p или git add --patch позволяет выбрать часть изменений в файлах, чтобы добавить их в индекс. Это полезно, когда нужно включить отдельные доработки,

Отменить коммит файла: 
    git rm --cached <file> 
    git reset HEAD <file>

Если забыли добавить файл в проект или опечатались в правках после коммита, не нужно создавать новый. Достаточно добавить изменения к последнему коммиту. Для этого используется опция --amend:
git commit --amend
git commit --amend -m "Текст вашего комментария"

# Выполняем первый коммит, в кавычках пишем комментарий
git commit -m "сhange homework.py" 
# Добавляем файлы в индекс Git 
git add . 
# Добавляем эти файлы в предыдущий коммит
git commit --amend -m "Add new files"

git push --force
принудительно обновить удалённую ветку, может привести к потере истории или данных. При применении этой команды история изменений на удалённом репозитории обновляется в соответствии с новыми изменениями в локальном репозитории. 

git reset HEAD 
переместить указатель HEAD на конкретный коммит. Отменяем изменения во всех файлах до последнего коммита. Все изменения в рабочем каталоге будут отменены, а сам каталог возвращён к состоянию в последнем коммите. Любые несохранённые изменения будут потеряны.
git reset --soft HEAD~B позволяет вернуться к определенному коммиту B

git reset HEAD file
перейти на один коммит назад в определённом файле, указав его имя через HEAD

! Важно: если вы использовали git push, чтобы отправить коммит на удалённый сервер и затем переопределили этот коммит с помощью git reset --soft, необходимо применить git push --force, чтобы отправить изменения на сервер. Мы не рекомендуем это делать, если вы работаете в общем репозитории, так как это может привести к проблемам синхронизации с другими участниками команды.

git reset --soft перемещает HEAD на указанный коммит, сохраняет промежуточную область и рабочий каталог.
git reset --mixed перемещает HEAD на указанный коммит, сбрасывает промежуточную область, но сохраняет рабочий каталог.
git reset --hard перемещает HEAD на указанный коммит, сбрасывает и промежуточную область, и рабочий каталог.

git branch -D ветка
удалить ветку

! Для объединения (смерживания) веток нужно сначала переключиться в ту ветку, в которую должны быть добавлены изменения, и только затем применить команду слияния.
git checkout master # Переключились на master.
git merge homework  # Перенести все коммиты из homework в ветку master

git rebase
когда надо сохранить историю коммитов
