@echo off
chcp 65001 >nul
echo ============================================================
echo   AI-Project-Template: Автоматическое развертывание окружения
echo ============================================================
echo.

:: 1. Проверка наличия Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ОШИБКА] Python не найден в системе!
    echo Установите Python 3.11+ с официального сайта python.org
    echo и ОБЯЗАТЕЛЬНО отметьте галочку "Add python.exe to PATH".
    pause
    exit /b 1
)

echo [1/4] Проверка Python: УСПЕШНО
python --version

:: 2. Создание виртуального окружения .venv (если еще не создано)
if not exist ".venv" (
    echo [2/4] Создание виртуального окружения .venv...
    python -m venv .venv
    if errorlevel 1 (
        echo [ОШИБКА] Не удалось создать виртуальное окружение .venv!
        pause
        exit /b 1
    )
) else (
    echo [2/4] Виртуальное окружение .venv уже существует.
)

:: 3. Обновление pip и установка зависимостей
echo [3/4] Установка зависимостей из requirements.txt...
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
if errorlevel 1 (
    echo [ВНИМАНИЕ] Возникли предупреждения при установке некоторых пакетов.
)

:: 4. Создание файла конфигурации .env из шаблона
if not exist ".env" (
    if exist ".env.example" (
        echo [4/4] Создание локального файла .env из .env.example...
        copy .env.example .env >nul
    )
) else (
    echo [4/4] Файл конфигурации .env уже присутствует.
)

echo.
echo ============================================================
echo [ПРОВЕРКА] Запуск проверочных тестов...
echo ============================================================
python -m unittest discover tests -v

echo.
echo ============================================================
echo   Развертывание завершено! Проект готов к работе.
echo   Для активации окружения вручную: call .venv\Scripts\activate
echo   Для запуска приложения: python -m src.main
echo ============================================================
echo.
pause
