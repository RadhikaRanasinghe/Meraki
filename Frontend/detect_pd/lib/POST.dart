import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'TesterModel.dart';

class PostRequestTest extends StatefulWidget {
  @override
  _PostRequestTestState createState() => _PostRequestTestState();
}

Future<TesterModel> createUser(String age, String gender, String handedness) async{
  // Todo: Assign the API host address to variable here
  // final String apiUrl = "https://localhost:127.2.2.5001/create_user";
  final String apiUrl = "https://reqres.in/api/users";

  final response = await http.post(apiUrl, body: {
    "age": age,
    "gender": gender,
    "handedness": handedness,
  });

  // Todo : Edit this block according to our API
  if(response.statusCode == 201) {
    final String responseString = response.body;
    return testerModelFromJson(responseString);
  } else {
    return null;
  }
}

class _PostRequestTestState extends State<PostRequestTest> {

  TesterModel _user;
  final TextEditingController ageController = TextEditingController();
  final TextEditingController genderController = TextEditingController();
  final TextEditingController handednessController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body:Container(
        padding: EdgeInsets.all(32),
        child: Column(
          children: <Widget>[
            Padding(padding: const EdgeInsets.only(
              bottom: 35,
            ),
              child: Text("Enter the following details",
                style: TextStyle(
                  fontSize: 20,
                  color: const Color(0xFF033E6B),
                ),
              ),
            ),
            TextField(
              controller: ageController,
              decoration: new InputDecoration(
                hintText: 'Age',
                icon: Icon(Icons.add),
              ),
            ),
            TextField(
              controller: genderController,
              decoration: new InputDecoration(
                hintText: 'Gender',
                icon: Icon(Icons.add),
              ),
            ),
            TextField(
              controller: handednessController,
              decoration: new InputDecoration(
                hintText: 'Handedness',
                icon: Icon(Icons.add),
              ),
            ),
            SizedBox(height: 32,),
            _user == null ? Container() :
            Text("The user : ${_user.age}, ${_user.gender}, ${_user.handedness}"),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () async{
          final String age = ageController.text;
          final String gender = genderController.text;
          final String handedness = handednessController.text;
          final TesterModel user = await createUser(age, gender, handedness);

          setState(() {
            _user = user;
          });
        },
        child: Icon(Icons.add),
      ),
    );
  }
}