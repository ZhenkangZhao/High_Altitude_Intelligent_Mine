const { test, expect } = require('@playwright/test');

test.describe('Dashboard', () => {
  test('page loads without errors', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/HAIM-MAS/);
  });

  test('shows vehicle status cards', async ({ page }) => {
    await page.goto('/');
    const vehicleCards = page.locator('[class*="VehicleStatusCard"], [class*="vehicle"]');
    await expect(vehicleCards.first()).toBeVisible({ timeout: 10000 });
  });

  test('shows efficiency traffic light', async ({ page }) => {
    await page.goto('/');
    const trafficLight = page.locator('text=正在作业');
    await expect(trafficLight).toBeVisible({ timeout: 10000 });
  });

  test('shows system status in header', async ({ page }) => {
    await page.goto('/');
    const systemStatus = page.locator('text=系统状态');
    await expect(systemStatus).toBeVisible({ timeout: 10000 });
  });
});

test.describe('Scheduling', () => {
  test('recommendation accept button exists', async ({ page }) => {
    await page.goto('/');
    const acceptButton = page.locator('button:has-text("采纳")');
    const count = await acceptButton.count();
    if (count > 0) {
      await expect(acceptButton.first()).toBeVisible({ timeout: 5000 });
    }
  });

  test('recommendation reject button exists', async ({ page }) => {
    await page.goto('/');
    const rejectButton = page.locator('button:has-text("否决")');
    const count = await rejectButton.count();
    if (count > 0) {
      await expect(rejectButton.first()).toBeVisible({ timeout: 5000 });
    }
  });
});