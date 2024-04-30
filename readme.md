# Links to closed issues:
[Issue One](https://github.com/#/event_manager/issues/1)
[Issue Two](https://github.com/#/event_manager/issues/5)
[Issue Three](https://github.com/#/event_manager/issues/7)
[Issue Four](https://github.com/#/event_manager/issues/9)
[Issue Five](https://github.com/#/event_manager/issues/11)
[Issue from Instructor Video](https://github.com/#/event_manager/issues/3)

  - Updated `readme.md`.
- Changed image name.
- Added DockerHub image.
- Updated `requirements.txt`.
- Adjusted `production.yml` further.
- Updated `production.yml`.
- Updated user schema tests for email validation.
- Updated user schema to properly test the example response data.
- Added HTTP validation for profile picture URL.
- Updated remaining user schema tests to use data from Docs page.
- Correctly tested for username validation in Docs page.
- Updated profile picture URL to correct URL.



# Reflection
I learned both proper github collaboration techniques and schema analysis/testing in this assignment. First off, I learned the proper workflow of making changes with git: Create an issue with a descritive title on GitHub, assign this to yourself, create a new branch from it, fetch and checkout to it on local, make changes, run tests, push to GitHub, create a pull request, have someone review the code (just me in this case, but usually someone else), and merge into other branch if everything checks out.

Secondly, the code I was reviewing for this project was the user model and user schemas. Its important to make sure the user schemas align with the user model. While checking for error in the user schema and Docs page, I got an overview of how sql alchemy is used in conjunction with the postgres databse. I also got experience running the entire project on Docker, from building the image, to running tests and migrations through Docker.