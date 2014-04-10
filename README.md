SE-Final-Project
================

Code repository for the "Improved Room of Requirement" project by Jin U Bak &amp; Nishant MC

(Work in progress! Project structure, MDD, code base, etc. coming soon)

Observer Views: We tried some DIY with GitStats. We set up a cron job to run a shellscript every week which uses GitStats to generate a report website, zips the generated files into a tarball, and e-mails the archive to Jin and myself. This turned out to be quite a pain to set up, and was not as fully featured as GitHub's contributor graphs.

Code Review: We tried some DIY with Gerrit for GitHub. The lesson we learned is DO NOT USE GERRIT FOR GITHUB. It is really buggy and hard to set up, and broke almost immediately. Review Board didn't seem to offer us anything we'd need. Instead, we're just falling back on GitHub's native features.

Bug Tracking: We looked into Trac, but seriously, this is a repo with a max of two contributors. To use that (or Bloodhound) would be like fighting Roman cavalry with MIG-47 fighter jets. Total overkill. We're falling back on Git's handicapped Issue Tracker - it's likely to be all we'll need.

Continuous Integration: Ah, this is one thing that GitHub actually doesn't give us for free. We're using a cool application called drone.io for this. If you sign up with your GitHub on their website we can give you Read access. If you'd like, we can also add your e-mail to the build alert list. Drone also provides some nicer issue tracking features than GitHub.
