const express = require('express');
const sqlite3 = require('sqlite3').verbose();

const flag = process.env.FLAG || 'flag{fake_flag}';

const app = express();
app.use(express.json());

const db = new sqlite3.Database(':memory:', (err) => {
  if (err) {
    console.error('Could not connect to database', err);
  }
});

db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT UNIQUE,
    opis TEXT
  )`);

  db.run(`INSERT INTO users (user, opis) VALUES ('admin', '`+flag+`')`);

  db.run(`CREATE TABLE IF NOT EXISTS diplomske (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    naslov TEXT,
    link TEXT,
    datum TEXT,
    povzetek TEXT,
    kategorija TEXT,
    fakulteta TEXT,
    uid TEXT
  )`);

  db.run(`INSERT INTO diplomske (naslov, link, datum, povzetek, kategorija, fakulteta, uid) VALUES
    ('Primer naloge 1', 'http://example.com/1', '2024-01-01', 'Povzetek naloge 1', 'Kategorija A', 'Fakulteta X', 'admin'),
    ('Primer naloge 2', 'http://example.com/2', '2024-02-01', 'Povzetek naloge 2', 'Kategorija B', 'Fakulteta Y', 'admin'),
    ('Primer naloge 3', 'http://example.com/3', '2024-03-01', 'Povzetek naloge 3', 'Kategorija A', 'Fakulteta X', 'admin')
  `);
});

const port = 8000;

app.get('/', (req, res) => {
  db.all('SELECT * FROM diplomske', [], (err, rows) => {
    if (err) {
      res.status(500).send('Error fetching data');
    } else {
      res.json(rows);
    }
  });
});

app.post('/insert', (req, res) => {
  const { naslov, link, datum, povzetek, kategorija, fakulteta, uid } = req.body;
  const sql = `INSERT INTO diplomske (naslov, link, datum, povzetek, kategorija, fakulteta, uid) VALUES (?, ?, ?, ?, ?, ?, ?)`;
  const params = [naslov, link, datum, povzetek, kategorija, fakulteta, uid];
  db.run(sql, params, function(err) {
    if (err) {
      res.status(500).send('Error inserting data');
    } else {
      res.status(201).send({ id: this.lastID });
    }
  });
});

app.get('/search', (req, res) => {
  let keys = req.query.keys?.split(',');
  if (!keys) keys = ['naslov', 'povzetek', 'kategorija', 'fakulteta'];
  keys = ['id', ...keys];
  const sql = `SELECT ${keys.join(', ')} FROM diplomske LIMIT 50`;
  db.all(sql, [], (err, rows) => {
    if (err) {
      res.status(500).send('Error fetching data');
    } else {
      res.json(rows);
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

