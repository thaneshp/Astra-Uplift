## Problem 

The aim of this project is to uplift Astra, a REST API penetration testing tool. The existing tool allows users to enter in their REST API, generating a report outlining the vulnerabilities that exist with their API. 

The intent of this project is to maintain this core functionality, while uplifting the application in the following ways:
- `python 2` to `python 3` upgrade
- Registration/login functionality
- Frontend/UI enhancement
- Performance Optimisation 
- Deployment to the internet

## Background

Developers (especially independent ones) aren't able to test their REST APIs in a cost efficient way. API penetration testing products are usually catering for enterprise customers which make it difficult for developers to purchase and use for self/open-source projects.

## In Scope

1. Entire codebase should be in `python 3`.
2. User registration/login functionality - scans should be associated to an individual user.
3. The interface should be easy-to-use and navigate, with a modern look and feel.
4. The amount of time taken to complete a scan should be significantly shorter than present.
5. Users should be able to use and interact with the application over the internet.

## Out of Scope

1. Handling of other types of APIs.

	Reason: Existing test cases are designed around common vulnerabilities within REST APIs. An entirely new set of test cases will need to be designed to handle other types of APIs.

2. Emailing of reports.

	Reason: Time could be better spent honing the core functionality for users to have a better experience. This can be added later if users have a preference for it.

## End-to-End User Flow

1. User develops a REST API
2. User deploys REST API 
3. User visits ProbeX via their web browser
4. User registers/logins in to their account
5. User is directed to the testing page
6. User enters the product name, REST API URL, Method, *Headers* and *Body*
7. The test is added to the list of **Recent Scans**, with a status of `In Progress`
8. ProbeX performs a series of tests on the user's input, generating a report
9. Once completed, the status of the test changes to `Completed`
10. User clicks on the completed test, which directs them to report's page
11. The report's page contains vulnerabilities associated with the user's REST API
12. User reads through report and determines which vulnerabilities are important to them
