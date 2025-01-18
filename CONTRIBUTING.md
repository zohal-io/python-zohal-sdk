# Contributing to YourPackageName

Thank you for considering contributing to **YourPackageName**! Contributions are what make open-source software great, and your help is highly appreciated.

## How to Contribute

### 1. Report Issues

If you encounter a bug, have a question, or want to suggest a feature:
- Check the [issues page](https://github.com/zohal/python-zohal-sdk/issues) to see if it has already been reported.
- If not, open a new issue with the following details:
  - **Title**: A concise description of the issue.
  - **Description**: Steps to reproduce the issue or the details of the feature request.
  - **Environment**: Include Python version, OS, and any other relevant information.

### 2. Submit Code Changes

#### Fork the Repository
1. Go to the [repository](https://github.com/zohal/python-zohal-sdk) and fork it.
2. Clone your fork:
   ```bash
   git clone https://github.com/your_username/your_fork.git
   cd your_fork
   ```

#### Create a Branch
Create a new branch for your changes:
```bash
git checkout -b feature/your-feature-name
```

#### Make Changes
- Follow the project's coding style (adhering to [PEP 8](https://www.python.org/dev/peps/pep-0008/)).
- Write clear and concise commit messages. Use present tense, e.g., "Add feature X."

#### Run Tests
Ensure your changes do not break existing functionality by running the test suite:
```bash
pytest
```
If you add a new feature, include relevant tests.

#### Push Changes
Push your changes to your forked repository:
```bash
git push origin feature/your-feature-name
```

#### Open a Pull Request
1. Go to the original repository and click "New Pull Request."
2. Select your branch and provide a clear description of your changes.


## Development Environment

To set up a local development environment:
1. Clone the repository.
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Run tests to confirm everything is working:
   ```bash
   pytest
   ```

## Thank You

Thank you for taking the time to contribute! Your efforts make this project better for everyone.
