# proxysqlctl
A controller to manage ProxySQL from the CLI.

This will also act as a framework for me to learn Python.

### Problem Statement:
ProxySQL currently has no way to manage it without logging into the MySQL-client interface directly, making changes, and loading those changes to the runtime state + saving them to disk.

There is nothing inherently wrong with this, I just find it clunky. This is purely an opinion.

Example of the clunkiness:
```
To create a user:
  INSERT INTO mysql_users (field, list) VALUES (the, values);
  LOAD MYSQL USERS TO RUN;
  SAVE MYSQL USERS FROM RUN; # This hashes the clear-text password if you didn't insert the raw hash, skip otherwise.
  SAVE MYSQL USERS TO DISK;
```
### The (very) rough plan:

* verb-noun format commandline because I'm a DBA (+ occasional SysAdmin) and like **act** on **things**.
  * `proxysqlctl create mysql user -u username ...` vs. `proxysqlctl mysql user create -u username ...`
  * The first example makes the most sense in english.
  * This will also likely be the hardest to implement. I am a frightfully amateur dev and the examples I've seen to implement this are.. whew. Over my head. For now.
* YAML-based configuration, probably stored in `~/.config/proxysqlctl/config.yaml`
  * I <3 yaml bigly
* Released as a contained, single file.
  * Undecided if I'll be using Bazel or pyinstaller.

 Eventually, we'll support ingesting secrets from GCP, AWS and Azure. Probably more in time.

### Challenges

1. Extremely low-skill developer (me).
2. Keeping up with ProxySQL's changes
3. ... I'm probably forgetting something.
