import 'package:flutter/material.dart';

/// Models:

/// Screens:

/// Widgets:

/// Services:

/// State:

/// Utils/Helpers:
import 'package:responsive_builder/responsive_builder.dart';

/// Entry Point:
class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: ScreenTypeLayout.builder(
          mobile: (BuildContext context) {
            return OrientationLayoutBuilder(
              // Force a screen to stay in portrait/landscape. Overrides the OrientationLayoutBuilder
              // mode: OrientationLayoutBuilderMode.portrait,
              portrait: (context) => Container(),
              landscape: (context) => Container(),
            );
          },
          tablet: (BuildContext context) {
            return OrientationLayoutBuilder(
              portrait: (context) => Container(),
              landscape: (context) => Container(),
            );
          },
          desktop: (BuildContext context) => Container(),
        ),
      ),
    );
  }
}
