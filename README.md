# Boss Dungeon Material Tracker

A comprehensive tracker for Dungeon Boss Materials and Titles, automatically synced daily from Google Sheets.

## 🌐 Live Site

**Visit:** https://liliikyu.github.io/Boss-Dungeon-Material-Tracker/

The site includes:
- 🏰 **Dungeons & Materials** - Browse all dungeons and their drops
- 👑 **Title Tracker** - Calculate remaining materials needed

## 📊 Data Sections

This tracker includes:
- **Dungeon Boss Materials** - Complete material drop information for all dungeons
- **Titles** - Title requirements and materials needed

## 🔄 Auto-Sync & Deployment

- **Data Sync:** Every day at 00:00 UTC from Google Sheets
- **Website Deploy:** Automatically deployed to GitHub Pages
- **Updates:** Changes appear within ~1 hour of sync completion

## 📁 Files

- `index.html` - Main unified dashboard (Dungeons + Titles)
- `dungeon_boss_material.csv` - Raw CSV data from Google Sheets
- `title_tracker.csv` - Title data from Google Sheets
- `.github/workflows/sync-sheets.yml` - Daily sync automation
- `.github/workflows/deploy-pages.yml` - GitHub Pages deployment

## 🚀 Features

### Dungeons & Materials Tab
- 🔍 Search dungeons by name or level
- 📋 View all drops for each dungeon
- 📊 Entry limits per day
- Expandable details

### Title Tracker Tab
- 👑 Calculate remaining materials needed
- 📝 Input current quantities
- ⚡ Auto-calculate remaining amounts
- 🔍 Search titles

## 📝 Source Data

Data comes from your Google Sheet:
- [Main Tracker Sheet](https://docs.google.com/spreadsheets/d/15aKwZohEpEwa9fOOnrcqZvAQ-JdHrVLcRTKglM2g1EQ/edit?usp=sharing)

**Sheets Synced:**
- Dungeon Boss Material (GID: 257026824)
- Title Tracker (GID: 1925983488)

## 🔧 How It Works

1. **You edit your Google Sheet** → Changes saved
2. **Daily GitHub Action runs** (00:00 UTC) → Pulls latest data
3. **CSVs update in repo** → Data downloads
4. **Pages auto-deploy** → Site updates automatically

## 📱 Responsive Design

- ✅ Works on desktop, tablet, and mobile
- ✅ Fast loading
- ✅ Searchable and filterable

## 🛠️ Setup Requirements

- ✅ Google Sheet is publicly accessible
- ✅ GitHub Actions enabled
- ✅ GitHub Pages enabled (Deploy from Branch: main)

---

**Last Data Sync:** Check the commit history for timestamps
