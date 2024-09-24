# Pelican-Twenty-Fifteen-Theme
WordPress Twenty Fifteen Theme for Pelican Satic Site Generator

---

### Introduction

Welcome to the **Twenty Fifteen Pelican Theme**! This theme is based on the popular WordPress Twenty Fifteen theme, but tailored specifically for Pelican. It’s designed with simplicity and speed in mind, making your site look great and load super fast. Whether you're blogging, sharing your projects, or building a portfolio, this theme has everything you need with modern SEO features and user-friendly design.

### Features

#### Minimal Design
Simplicity is key. The theme has a clean, minimal design that’s easy on the eyes. It keeps the focus on your content without unnecessary distractions.

#### Super Fast Loading
Nobody likes a slow website! This theme is optimized for speed, so your pages load incredibly fast, keeping visitors happy and improving your site’s performance.

#### Sitemap
Easily generate a sitemap for your site. This helps search engines like Google to better index your content, improving your visibility online.

#### HTML/CSS Minification
Your site's code is automatically compressed, making it smaller and faster to load without affecting the design or functionality.

#### Quicklink Support
Thanks to **Quicklink**, when someone visits your site, it preloads links they might click next. This means those pages will open lightning fast when they’re ready to explore more.

### SEO Features

#### Optimized for SEO
The theme is built with search engine optimization in mind. It's designed to make your content rank higher in search engines, helping more people find your site.

#### Robots Meta Tag
You can control the visibility of each post or page with the robots meta tag. It’s easy to add on a per-page or per-post basis, so you can tell search engines what to index and what to ignore.

#### Noindex for Useless Pages
Certain pages, like navigation or category pages, aren’t useful for search engines, so the theme adds **noindex** automatically to them. This keeps your site cleaner in search results.

#### Disqus Comments
Engage with your readers through **Disqus**! The theme integrates with Disqus comments, making it easy for visitors to leave feedback and start discussions on your posts.

#### Google Analytics Support
Track your website traffic with **Google Analytics**! This theme makes it simple to set up, so you can see who’s visiting your site and how they’re engaging with your content.


This theme gives you the perfect mix of speed, simplicity, and powerful SEO tools, all wrapped in a clean, user-friendly package.

---

## How to edit the pelicanconf config

Edit the below config in pelicanconf.py - 

```jinja
AUTHOR = 'Layouts Hub'
SITENAME = "Layouts Hub"
SITEURL = "https://layoutshub.github.io/pelican-twenty-fifteen-theme"
SITE_LOGO_URL = "YOUR_SITE_LOGO"
SITE_SUMMARY = "A collection of Pelican, Jekyll, Hugo, Gatsby theme. Ported themes from other cms."

# TimeZone, Replace 'Europe/Rome' with your preferred TIMEZONE.
TIMEZONE = 'Europe/Rome'

# Disqus Comment Plugin
DISQUS_USERNAME = None

# Google Analytics Tracking
GOOGLE_ANALYTICS_ID = None
```


## How to edit the publishconf config

Edit the below line publishconf.py -

```jinja
SITEURL = "https://layoutshub.github.io/pelican-twenty-fifteen-theme/"

# Disqus Comment Plugin
DISQUS_USERNAME = None

# Google Analytics Tracking
GOOGLE_ANALYTICS_ID = None
```

---

### Article Page Tags

When creating an article page in the **Twenty Fifteen Pelican Theme**, you need to include specific metadata at the top of each page to ensure it displays correctly and is optimized for SEO. Here’s a breakdown of the required tags and how they work:

```markdown
---
title: What is Lorem Ipsum?  
summary: Summary of the post  
featured_image: https://placehold.co/600x400/EEE/31343C  
category: ispum  
slug: what-is-loreum-ispum  
date: 14/09/2024  
robots: index, follow  
status: published  
---
```

### Explanation of Tags:

1. **`title`**:  
   The title of your article. This will be displayed as the heading on the page and in search results.
   - Example: `title: What is Lorem Ipsum?`

2. **`summary`**:  
   A brief summary of the post, which is often shown in post listings and previews. This gives readers a quick overview of the content.
   - Example: `summary: Summary of the post`

3. **`featured_image`**:  
   A URL to the image that will be featured with your post. This is often displayed at the top of the article or in previews.
   - Example: `featured_image: https://placehold.co/600x400/EEE/31343C`

4. **`category`**:  
   The category that this article belongs to. This helps organize content and makes it easier for readers to find related posts.
   - Example: `category: ispum`

5. **`slug`**:  
   The part of the URL that uniquely identifies the article. It is automatically generated from the title, but you can specify it manually. This should be in lowercase with hyphens instead of spaces.
   - Example: `slug: what-is-loreum-ispum`

6. **`date`**:  
   The publication date of the post. Format this as `DD/MM/YYYY`.
   - Example: `date: 14/09/2024`

7. **`robots`**:  
   This tag tells search engines whether they should index and follow the post. Use `index, follow` to allow search engines to list the post, or `noindex, nofollow` if you don’t want the post to be indexed.
   - Example: `robots: index, follow`

8. **`status`**:  
   The status of the post. Use `published` to make the post live, or `draft` to keep it hidden until it's ready.
   - Example: `status: published`


By including these tags at the top of each article, you can easily manage the post’s title, summary, featured image, author information, and SEO settings.

---

### Static Pages Tags

For static pages like "About" in the **Twenty Fifteen Pelican Theme**, you need to include specific metadata to ensure these pages display properly and are optimized for search engines. Here’s how you should structure the metadata for static pages:

```markdown
---
title: About  
slug: about  
summary: This is my about us page  
featured_image: https://placehold.co/600x400/EEE/31343C  
robots: index, follow  
status: published  
---
```

### Explanation of Tags:

1. **`title`**:  
   The title of the static page, which will appear as the heading of the page and in the browser tab.
   - Example: `title: About`

2. **`slug`**:  
   The unique part of the URL for the page. It helps to define where this page will be accessible. For an "About" page, the slug is usually simple, like `/about`.
   - Example: `slug: about`

3. **`summary`**:  
   A short description or summary of the static page. This can be useful for previews or post listings.
   - Example: `summary: This is my about us page`

4. **`featured_image`**:  
   A URL to the image that will be featured on the page. This can enhance the page visually or help with SEO.
   - Example: `featured_image: https://placehold.co/600x400/EEE/31343C`

5. **`robots`**:  
   This tag tells search engines whether they should index the page and follow links on it. Use `index, follow` to allow search engines to list the page, or `noindex, nofollow` if you want to exclude it from search results.
   - Example: `robots: index, follow`

6. **`status`**:  
   Indicates the publication status of the page. Use `published` to make the page live, or `draft` to keep it hidden until you’re ready.
   - Example: `status: published`


By including these tags, you ensure that your static pages, like "About," are organized, indexed by search engines, and easy to manage in Pelican.

---

### License

The **Twenty Fifteen Pelican Theme** is licensed under the **GPL (General Public License)**, originally released by WordPress. This means you are free to use, modify, and distribute the theme as you see fit, as long as you adhere to the terms of the GPL.

#### License Details:
- **License Type**: GPL (General Public License)
- **Original Source**: WordPress Twenty Fifteen Theme

### No Guarantee
Please note that while this theme has been ported and optimized for Pelican, it is provided "as is" without any guarantees or warranties. The developers are not responsible for any issues that may arise from using this theme, including but not limited to performance, compatibility, or data loss.

Feel free to contribute to its development or suggest improvements, but please do so in the spirit of open-source collaboration!


## Developer Contacts
1. Twitter - https://twitter.com/vishalchopra666

---

### Contributing

Feel free to **fork**, **pull**, and **contribute** to the **Twenty Fifteen Pelican Theme**! We welcome any improvements, bug fixes, or new features that can enhance this theme for everyone. Your contributions help make this project better and more useful to the community.

### Thank You!
Thank you for using and supporting this theme! Enjoy building your website with it, and happy blogging!