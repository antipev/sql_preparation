## Linting Requirements

### Lint Your SQL

Our team's SQL style standard is configured in the `.sqlfluff` file in this repository.

For details on each rule and how to configure them, refer to the [SQLFluff Rules Documentation](https://docs.sqlfluff.com/en/stable/reference/rules.html).

To check your SQL files for style violations, run the following command:

```bash
sqlfluff lint .
```

To lint a specific file or directory, specify the path:

```bash
sqlfluff lint folder/model.sql
sqlfluff lint folder
```

### Fix Your SQL

To automatically fix linting errors where possible, use the `fix` command:

```bash
sqlfluff fix .
```

To fix a specific file or directory:

```bash
sqlfluff fix folder/model.sql
sqlfluff fix folder
```

#### ⚠️ Note:

The sqlfluff fix command modifies your files, so it's always a good practice to review the changes and run `dbt compile` afterward to ensure no syntax errors were introduced.

#### 📝 Disabling rules:

Sometimes sqlfluff fix may not format your code as you'd like. In these cases, you can disable specific rules for a file or a line of code `using --noqa:`  or `-- noqa: disable=`. For example:

```sql
-- Ignore rule CP02 & rule CP03
SeLeCt  1 from tBl ;    -- noqa: CP02,CP03

```
For more details, refer to [Ignoring Errors & Files](https://docs.sqlfluff.com/en/latest/configuration/ignoring_configuration.html)

---

### Lint your YAML

Our team's YAML style standard is configured in the `.yamllint` file.

To check your YAML files for style violations, use the `yamllint` command:

```bash
yamllint .
```

To lint a specific file or directory:

```bash
yamllint folder/property.yml

yamllint folder
```

`yamllint` does not have an auto-fix feature. You will need to manually fix violations based on the error messages.

---

### Using `pre-commit`

We have added `sqlfluff` and `yamllint` to `.pre-commit-config.yaml`. You will need to fix violations to be able to commit your code changes.

Every time you run `git commit`, `pre-commit` will automatically run `sqlfluff` and `yamllint` on your staged files. If any violations are found, the commit will be blocked, and you will be prompted to fix them. You'll need to fix all violations to be able to commit your changes.

#### 💡 Best practice:

To avoid failed commits, it's recommended to run the sqlfluff lint and yamllint commands on your files before staging them. This allows you to catch and fix any issues before pre-commit runs its checks.

#### 🛠️ Troubleshooting a failed commit:

If your commit fails without a helpful error message, you can run `pre-commit` manually to see and fix the issue. Run the following command, and `pre-commit` will automatically fix simple violations for all files:

```bash
pre-commit run --all-files
```
After the command runs, stage the changes again (`git add .`) and then `git commit`.
