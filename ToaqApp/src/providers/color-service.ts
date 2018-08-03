//import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

/*
  Generated class for the ColorService provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class ColorService {
  trafficColors: any[] ; 
//public http: HttpClient
  constructor() {
    this.trafficColors = ["red", "green", "yellow" , "green"] ; 
  }

  getColors(){
    return this.trafficColors ; 
  }

}
