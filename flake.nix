{
  description = "patcher";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs?ref=nixpkgs-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    utils,
  }: (utils.lib.eachSystem ["x86_64-linux"] (system: rec {
    packages = {
      pythonEnv =
        nixpkgs.legacyPackages.${system}.python3.withPackages
        (ps: with ps; []);
    };
    pkgs.python3Packages.buildPythonPackage = {
      name = "patcher";
      src = ./.;
      propagatedBuildInputs = [(nixpkgs.legacyPackages.${system}.python3.withPackages (ps: with ps; []))];
    };
    defaultPackage = packages.pythonEnv; # If you want to just build the environment
    devShell = packages.pythonEnv.env; # We need .env in order to use `nix develop`
    shellHook = ''
      echo here's an example, betch.
      python patcher.py --universe 1 --start_dmx 1 --fixture_start 2001 --quantity 16 --width 18 --mode "Mode 6" --name_prefix "Vortex"
      python patcher.py --universe 1 --start_dmx 289 --fixture_start 2017 --quantity 16 --width 20 --mode "Profile 7" --name_prefix "S360"
    '';
  }));
}
