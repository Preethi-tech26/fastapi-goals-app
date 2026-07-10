# Playwright API Testing Cheat Sheet (TypeScript)

Personal reference based on the Goals API test suite.

---

## Setup

**Install Playwright:**
```
npm init -y
npm install -D @playwright/test
npx playwright install
```

**Run tests:**
```
npx playwright test
```

**Run with visible output:**
```
npx playwright test --reporter=line
```

**Generate and view HTML report:**
```
npx playwright test --reporter=html
npx playwright show-report
```

---

## Project Structure

```
playwright-goals-tests/
├── tests/
│   └── goals.spec.ts      # test files
├── playwright.config.ts   # config
├── package.json
└── .gitignore
```

**.gitignore — always include these:**
```
node_modules/
playwright-report/
test-results/
```

---

## playwright.config.ts

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  use: {
    baseURL: 'https://your-api.onrender.com',
    extraHTTPHeaders: {
      'Content-Type': 'application/json',
    },
  },
  reporter: 'html',
});
```

- `baseURL` — set once here, use relative paths (`/goals`) in tests
- `extraHTTPHeaders` — default headers for all requests
- `reporter` — `'html'` for visual report, `'line'` for terminal output

---

## Test Structure

```typescript
import { test, expect } from '@playwright/test';

test('description of what this test does', async ({ request }) => {
  // your test code here
});
```

- `test(...)` — defines a single test case
- `request` — Playwright's built-in API testing tool
- `async/await` — all requests are asynchronous

---

## Making API Requests

**GET request:**
```typescript
const response = await request.get('/goals');
```

**POST with JSON body:**
```typescript
const response = await request.post('/goals', {
  data: { title: 'My goal' }
});
```

**POST with form data (e.g. login endpoint):**
```typescript
const response = await request.post('/login', {
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  data: `username=prith&password=test123`
});
```

**Request with Authorization header:**
```typescript
const response = await request.post('/goals', {
  headers: { 'Authorization': `Bearer ${token}` },
  data: { title: 'Authenticated goal' }
});
```

**PUT request:**
```typescript
const response = await request.put(`/goals/${goalId}?completed=1`, {
  headers: { 'Authorization': `Bearer ${token}` }
});
```

**DELETE request:**
```typescript
const response = await request.delete(`/goals/${goalId}`, {
  headers: { 'Authorization': `Bearer ${token}` }
});
```

---

## Assertions (expect)

**Check status code:**
```typescript
expect(response.status()).toBe(200);
expect(response.status()).toBe(401);
expect(response.status()).toBe(404);
```

**Parse and check response body:**
```typescript
const body = await response.json();
expect(body.message).toBe('Welcome to the Goals API');
expect(body.message).toContain('created successfully');
expect(body.access_token).toBeTruthy();   // exists and not empty
expect(body.completed).toBe(0);
```

**Check array contents:**
```typescript
const goals = await response.json();
const hasGoal = goals.some((g: any) => g.title === 'My goal');
expect(hasGoal).toBe(false);   // user should NOT see this goal
```

---

## Common Patterns

**Get a token (register + login flow):**
```typescript
const username = `testuser_${Date.now()}`;  // unique username each run

await request.post('/register', {
  data: { username, password: 'test123' }
});

const loginResponse = await request.post('/login', {
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  data: `username=${username}&password=test123`
});

const { access_token } = await loginResponse.json();
```

**Use Date.now() for unique usernames:**
```typescript
const username = `testuser_${Date.now()}`;
// Generates something like: testuser_1718456789123
// Avoids "username already exists" errors on repeated test runs
```

**Test unauthorized access:**
```typescript
const response = await request.post('/goals', {
  data: { title: 'Should fail' }
  // No Authorization header
});
expect(response.status()).toBe(401);
```

**Test data isolation between users:**
```typescript
// Create goal as user 1
// Login as user 2
// GET goals as user 2
// Verify user 1's goal is NOT in the response
const goals = await response.json();
const hasUser1Goal = goals.some((g: any) => g.title === 'User 1 private goal');
expect(hasUser1Goal).toBe(false);
```

---

## Common Status Codes to Test

| Code | Meaning | When to expect it |
|------|---------|-------------------|
| 200 | Success | Valid requests |
| 401 | Unauthorized | Missing or invalid token |
| 404 | Not found | Resource doesn't exist |
| 422 | Unprocessable | Invalid input data |

---

## Git Gotchas for Playwright Projects

**node_modules always in .gitignore:**
```
node_modules/
playwright-report/
test-results/
```

**If node_modules got committed by mistake:**
```
rm -rf .git          # nuclear option — wipe history
git init             # start fresh
git add .
git commit -m "Initial commit"
```

**Check what's tracked:**
```
git ls-files
```

**Check repo size:**
```
git count-objects -vH
```
Should be small (KiB range) for a test project — if it's MiB, node_modules crept in.

---

## Tests Written So Far

| Test | What it covers |
|------|----------------|
| Health check | GET / returns 200 and correct message |
| Register user | POST /register creates user successfully |
| Login | POST /login returns JWT token |
| Create goal (authenticated) | POST /goals with token works |
| Unauthorized access | POST /goals without token returns 401 |
| Data isolation | User 2 cannot see User 1's goals |
