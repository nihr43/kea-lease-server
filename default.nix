{ nixpkgs ? import <nixpkgs> {  } }:

let
  pkgs = with nixpkgs.python312Packages; [
    flask
  ];

in
  nixpkgs.stdenv.mkDerivation {
    name = "env";
    buildInputs = pkgs;
  }
