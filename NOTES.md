# Fast Dev DevOps

## GOAL/AUDIENCE

- as a developer or devops person
- get you up to speed on delivering quality software rapidly
- overall techniques and workflow to help keep you focused
  
## Fast Dev

=> MLG - FBL - loop value, entr, TDD ; assert, breakpoint

### Min Lag Gap

Optimize two functions:
* MIN LAG = deliver something in fast iterations
* MIN GAP = get closer to biz expectations
  * if it changes that's fine

### Feedback Loop

Do something, see the result

### Loop Value

One way is to test the software manually.
* slow value, slow eval, super easy
Min Lag Gap: let's min lag...
- Let's just put a function in a loop and see how it changes
- => no longer have to think about test, we just make changes, save it, and get the result in a few seconds
- (doesn't work for teams, inconsistent btw devs)
- (save into Makefile/shell/invoke)

### Entr

Value loop is awkward, let's get value when files change.
Min Lag again.
* entr

### TDD

- work at higher level (given/when/then)
- ? Red/Green/Refactor
  - state: read/write JSON; then move to class; then switch to SQL
- focus on single function (unit test)
- (later: workflow with advanced pytest)
- connect effort to _biz_ value
  - don't get lost
  - ? don't add quality if they can't see it?
  - Always Be Demoing

## INBOX

- loop (loopm)

## OUTBOX

- Selenium
  - too hard to install
