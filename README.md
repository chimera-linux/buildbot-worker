# Chimera buildbot worker

This is the [buildbot](https://buildbot.net/) worker as used in Chimera's
infrastructure.

To set up, just create a plain worker and add the files from inside of this
repo.

A `user_config.py` must be present. A sample file is included in this repo.

If you wish to use TLS with self-signed cert, you need the certificate PEM
file present on the worker, in the example in the `ca-certs` directory.

## Additional worker setup

You will also need a `cbuild` configuration on your worker. The expectations
for this are defined by the master. Typically this means a `config.ini`
for `cbuild` present in the path that the master expects. The configuration
file can then define all other aspects of the `cbuild` invocation, which
are chosen by the worker.

The config file can look like this:

```
[apk]
command = ~/cbuild/apk.static

[build]
build_root = ~/cbuild/bldroot
cbuild_cache_path = ~/cbuild/cache
repository = ~/cbuild/packages
stage_repository = ~/cbuild/pkgstage
sources = ~/cbuild/sources
ccache = yes
check = yes
remote = no

[signing]
key = ~/cbuild/keys/foo.rsa
```

A full packages repository must also be present on the worker, in the
location expected by the master as well as by the config file above.
