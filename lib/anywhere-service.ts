import { BaseService, CfnService, Ec2Service, Ec2ServiceProps } from "@aws-cdk/aws-ecs";
import { Construct } from "@aws-cdk/core";

export class AnywhereService extends Ec2Service {
    constructor(scope: Construct, id: string, props: Ec2ServiceProps) {
        super(scope,id,props);
        (this.node.defaultChild as CfnService).launchType='EXTERNAL';
    }

    protected validate(): string[] {
        return [];
      }
}