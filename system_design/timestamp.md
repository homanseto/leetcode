# TimeStamp in database(PostGreSQL) with Coordinate Universal Time(UTC) for Global CRUD Workflow:

PostgreSQL always converts the incoming timestamp to UTC (UTC+0) before writing it to disk when using the TIMESTAMPTZ data type.
Automatic UTC normalization: When you insert data, PostgreSQL automatically converts any incoming time to UTC and stores it as a absolute point in time.
Prevents server-bias bugs: TIMESTAMP WITHOUT TIME ZONE strips away the context. If an engineer forgets to append 'UTC' during a manual insert, the database will assume the server's local time zone, corrupting your data.
Safer analytics: SQL queries that aggregate data across different global regions will automatically calculate correctly because the base data is explicitly recognized by the engine as UTC.

# Setup: Database Schema

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    timezone VARCHAR(50) NOT NULL -- Stores IANA names like 'America/New_York'
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    content TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

# INSERT (Creating Data)

# Option A (Let DB Handle It): Do not send a time from your app. Let the database generate it.

```sql
INSERT INTO posts (user_id, content) VALUES (1, 'Hello World');
-- created_at automatically becomes current UTC time.
```

# Option B (App Sends It): If the app must generate the time, convert it to an ISO string with a Z (UTC marker) or explicit offset before sending.

```sql
-- Application sends: '2026-06-25T04:15:00Z'
INSERT INTO posts (user_id, content, created_at) VALUES (1, 'Hello World', '2026-06-25T04:15:00Z');
```

# UPDATE (Modifying Data): When updating data or tracking an updated_at field, always push the current UTC time.

```sql
PDATE posts
SET content = 'Updated text', updated_at = CURRENT_TIMESTAMP
WHERE id = 5; d
```

# DELETE (Removing Data): Deleting rows doesn't usually require timezone calculations. However, if you use a Soft Delete pattern (deleted_at), treat it exactly like an update

```sql
UPDATE posts
SET deleted_at = CURRENT_TIMESTAMP
WHERE id = 5;
```

# GET (Retrieving Data): This is where the magic happens. The database holds raw UTC, and the application shapes it for the user. Database Query: Select the raw UTC data along with the user's preferred timezone.

```sql
SELECT p.content, p.created_at, u.timezone
FROM posts p
JOIN users u ON p.user_id = u.id
WHERE p.id = 5;
-- Returns: '2026-06-25 04:15:00+00' and 'America/New_York'
```

# Application Conversion Layer: Your backend or frontend takes that raw UTC timestamp and applies the user's IANA string to format it.

```javascript
const rawUtc = "2026-06-25T04:15:00Z";
const userTimezone = "America/New_York";

const localizedTime = new Date(rawUtc).toLocaleString("en-US", {
  timeZone: userTimezone,
});
console.log(localizedTime); // Outputs: "6/25/2026, 12:15:00 AM" (Accounts for DST automatically)
```

```python
from datetime import datetime
from zoneinfo import ZoneInfo

utc_time = datetime.fromisoformat("2026-06-25T04:15:00+00:00")
user_time = utc_time.astimezone(ZoneInfo("America/New_York"))
print(user_time.strftime("%Y-%m-%d %H:%M:%S")) # Outputs localized time

```
