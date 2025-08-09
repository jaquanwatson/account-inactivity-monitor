# Contributing to Account Inactivity Monitor

Thank you for your interest in contributing to Account Inactivity Monitor! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and considerate of others.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported by searching the [Issues](https://github.com/jaquanwatson/account-inactivity-monitor/issues).
2. If the bug hasn't been reported, [open a new issue](https://github.com/jaquanwatson/account-inactivity-monitor/issues/new/choose) using the Bug Report template.
3. Provide a clear title and description, along with steps to reproduce the bug.
4. Include any relevant screenshots or error messages.

### Suggesting Features

1. Check if the feature has already been suggested by searching the [Issues](https://github.com/jaquanwatson/account-inactivity-monitor/issues).
2. If the feature hasn't been suggested, [open a new issue](https://github.com/jaquanwatson/account-inactivity-monitor/issues/new/choose) using the Feature Request template.
3. Provide a clear title and description of the feature.
4. Explain why this feature would be valuable to the project.

### Pull Requests

1. Fork the repository.
2. Create a new branch from `main` for your changes.
3. Make your changes, following the coding standards and guidelines.
4. Add tests for your changes if applicable.
5. Ensure all tests pass.
6. Update documentation if necessary.
7. Submit a pull request to the `main` branch.

## Development Setup

1. Clone the repository:
   ```powershell
   git clone https://github.com/yourusername/account-inactivity-monitor.git
   cd account-inactivity-monitor
   ```

2. Install required PowerShell modules:
   ```powershell
   Install-Module Microsoft.Graph -Force
   Install-Module AzureAD -Force
   ```

3. Set up configuration:
   ```powershell
   Copy-Item config.example.json config.json
   # Edit config.json with your settings
   ```

4. Run tests:
   ```powershell
   Invoke-Pester
   ```

## Coding Standards

- Follow PowerShell best practices and style guidelines.
- Use meaningful variable and function names.
- Write comment-based help for all functions.
- Include error handling for all operations.
- Keep functions focused on a single responsibility.
- Use proper PowerShell verbs for function names.

## Security Considerations

- Never hardcode credentials in scripts.
- Always use secure methods for handling authentication.
- Follow the principle of least privilege for all operations.
- Implement proper error handling and logging.
- Be cautious with sensitive data like account information.

## Testing

- Write Pester tests for new functionality.
- Ensure all tests pass before submitting a pull request.
- Include tests for error conditions and edge cases.
- Test in both Active Directory and Microsoft 365 environments when applicable.

## Documentation

- Update documentation for any changes to functionality.
- Use comment-based help for all functions.
- Include examples in documentation.
- Document any configuration parameters.

## Review Process

1. All pull requests will be reviewed by the maintainers.
2. Feedback may be provided for necessary changes.
3. Once approved, the pull request will be merged.

Thank you for contributing to Account Inactivity Monitor!