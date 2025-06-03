# devenv.nix
{ pkgs, ... }:

{
  name = "Python project template";

  # https://devenv.sh/packages/
  packages = [
  ];

  # Set any environment variables here.
  # https://devenv.sh/reference/options/#env
  # env.TEST_ENV_VAR_1="foo";
  # env.TEST_ENV_VAR_2="bar";

  # Secrets can be set in a .env file. Change to true if needed.
  # https://devenv.sh/reference/options/#dotenvenable
  dotenv.enable = false;

  # https://devenv.sh/languages/
  languages.python.enable = true;
  languages.python.venv.enable = true;
  languages.python.uv = {
    enable = true;
    sync.enable = true;
    sync.allExtras = true; # Sync dev dependencies
  };

  # See full reference at https://devenv.sh/reference/options/
}
