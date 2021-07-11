import { expect as expectCDK, matchTemplate, MatchStyle } from '@aws-cdk/assert';
import * as cdk from '@aws-cdk/core';
import * as T3 from '../lib/t3-stack';

test('Empty Stack', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new T3.T3Stack(app, 'MyTestStack');
    // THEN
    expectCDK(stack).to(matchTemplate({
      "Resources": {}
    }, MatchStyle.EXACT))
});
