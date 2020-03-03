import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { inject } from '@angular/core/testing';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators'

@Injectable({
    providedIn: 'root'
})
export class ConfigService{
    constructor (private httpClient :HttpClient){}

    getBasicInfo():any
    {
        
        return this.httpClient.get("http://localhost:5002/getbasicinfo").pipe(map((resp:Response) => {return resp}))
    }

}