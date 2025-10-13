# devenv.nix
{ pkgs, ... }:

{
  name = "Python project template";

  # https://devenv.sh/packages/
  packages = [
    pkgs.go-task
  ];

  # Set any non-secret environment variables here.
  # https://devenv.sh/reference/options/#env
  env.PYTHONPYCACHEPREFIX=".pycache";  # Put bytecode files in a single folder

  # Secrets can be set in a .env file. Change to false if not needed.
  # https://devenv.sh/reference/options/#dotenvenable
  dotenv.enable = true;

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    venv.enable = true;
    version = "3.13.5";
  };
  languages.python.uv = {
    enable = true;
    sync.enable = true;
    sync.allExtras = true;  # Sync dev dependencies
  };

  enterShell = ''
    uv sync
    if [[ -d .git ]]; then
      pre-commit install -f --hook-type pre-commit --hook-type pre-push
    fi
  '';

  # See full reference at https://devenv.sh/reference/options/
}
