# Production Packaging Checklist

This checklist is designed for shipping the unlock tool as a cross-platform desktop application.

## Build preparation
- [ ] Confirm the repository is up to date and all functionality is tested.
- [ ] Run the complete automated test suite: `./run_tests.sh` or `run_tests.bat`.
- [ ] Confirm `README.md` and `EULA.txt` are current.
- [ ] Ensure `release_config.md` exists and keystore credentials are backed up.

## Desktop executable packaging
- [ ] Install PyInstaller in a clean packaging environment.
- [ ] Build the application from `build.spec`.
- [ ] Verify `devices.json`, `drivers/`, and `EULA.txt` are bundled.
- [ ] Test the output distribution on Windows, Linux, and macOS.
- [ ] Run `scripts/post_install.sh` or `scripts/post_install.bat` after installation.

## Android admin APK
- [ ] Build the release APK with Gradle using `assembleRelease`.
- [ ] Sign the APK with `scripts/sign_apk.sh` or `scripts/sign_apk.bat`.
- [ ] Confirm `zipalign` was applied successfully.
- [ ] Keep the signing keystore secure and backed up.

## License and blacklist server
- [ ] Deploy a static `revoke.txt` endpoint for license revocation.
- [ ] Confirm `core/license_manager.py` can fetch blacklist at runtime.
- [ ] Test offline fallback using only local `revoke.txt`.
- [ ] Use Netlify or another static host to serve `revoke.txt` from a stable URL.

## Updater and release server
- [ ] Host `version.json` at the configured update URL.
- [ ] Include package URLs for Windows, Linux, and macOS.
- [ ] Confirm update check and download path work without replacing the running executable.
- [ ] Deploy `netlify/version.json` and verify it is accessible immediately after publishing.

## Legal and support
- [ ] Ensure EULA acceptance is presented on first run.
- [ ] Confirm the EULA is stored in the user config.
- [ ] Add a support contact or issue reporting flow.

## Final verification
- [ ] Test on at least 5 physical devices across Android/iOS.
- [ ] Verify logging and crash reporting work.
- [ ] Export logs using the built-in menu and confirm archive creation.
- [ ] Validate the final release package on clean machines.
