import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class GetRequest extends StatelessWidget {

  // Todo: check if this method should be Future<>
  getRequest() async {
    //async function to perform http get
    final response = await http.get('http://127.0.0.1:5000/retrieve_result'); //getting the response from our backend server script
    final decoded = json.decode(response.body) as Map<String, dynamic>; //converting it from json to key value pair

    // Todo: complete method - if the result is positive display positive page, else display negative
    void checkResult() {
      if (decoded['Result'] == true) {
        // display positive results page
      } else {
        // display negative results page
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    throw UnimplementedError();
  }
}