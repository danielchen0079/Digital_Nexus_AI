Param (
    [string]$ProjectName = "PO"
)

#-------------------------------------
# 创建项目文件夹
#-------------------------------------

Write-Host "Creating project folder: $ProjectName"
New-Item -ItemType Directory -Force -Path $ProjectName | Out-Null
Set-Location -Path $ProjectName

#-------------------------------------
# 初始化 npm
#-------------------------------------

Write-Host "Initializing npm..."
npm init -y

#-------------------------------------
# 安装 Playwright
#-------------------------------------

Write-Host "Installing Playwright..."
npm install -D @playwright/test
npx playwright install

#-------------------------------------
# 创建标准文件夹
#-------------------------------------

$folders = @(
    ".github",
    ".github\workflows",
    "tests",
    "tests-examples",
    "pageObjects"
)

foreach ($folder in $folders) {
    Write-Host "Creating folder: $folder"
    New-Item -ItemType Directory -Force -Path $folder | Out-Null
}

#-------------------------------------
# 创建 .gitignore
#-------------------------------------

$gitignore = @"
node_modules/
playwright-report/
test-results/
"@

Write-Host "Creating .gitignore..."
$gitignore | Out-File -Encoding utf8 ".gitignore"

#-------------------------------------
# 创建 playwright.config.js
#-------------------------------------

$pwConfig = @"
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    trace: 'on-first-retry',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    }
  ],
});
"@

Write-Host "Creating playwright.config.js..."
$pwConfig | Out-File -Encoding utf8 "playwright.config.js"

#-------------------------------------
# 创建 GitHub Actions workflow (可选)
#-------------------------------------

$workflow = @"
name: Playwright Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npx playwright test
"@

Write-Host "Creating GitHub Actions workflow..."
$workflow | Out-File -Encoding utf8 ".github\workflows\playwright.yml"

Write-Host ""
Write-Host "✅ Playwright project structure has been created successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:"
Write-Host "1. cd $ProjectName"
Write-Host "2. npx playwright test"

//.\init-playwright.ps1
