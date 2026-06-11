"""Contains all the data models used in inputs/outputs"""

from .slurmdb_v0043_post_users_association_flags import SlurmdbV0043PostUsersAssociationFlags
from .v0043_account import V0043Account
from .v0043_account_flags_item import V0043AccountFlagsItem
from .v0043_accounting import V0043Accounting
from .v0043_accounting_allocated import V0043AccountingAllocated
from .v0043_assoc import V0043Assoc
from .v0043_assoc_default import V0043AssocDefault
from .v0043_assoc_flags_item import V0043AssocFlagsItem
from .v0043_assoc_max import V0043AssocMax
from .v0043_assoc_max_jobs import V0043AssocMaxJobs
from .v0043_assoc_max_jobs_per import V0043AssocMaxJobsPer
from .v0043_assoc_max_per import V0043AssocMaxPer
from .v0043_assoc_max_per_account import V0043AssocMaxPerAccount
from .v0043_assoc_max_tres import V0043AssocMaxTres
from .v0043_assoc_max_tres_group import V0043AssocMaxTresGroup
from .v0043_assoc_max_tres_minutes import V0043AssocMaxTresMinutes
from .v0043_assoc_max_tres_minutes_per import V0043AssocMaxTresMinutesPer
from .v0043_assoc_max_tres_per import V0043AssocMaxTresPer
from .v0043_assoc_min import V0043AssocMin
from .v0043_assoc_rec_set import V0043AssocRecSet
from .v0043_assoc_short import V0043AssocShort
from .v0043_coord import V0043Coord
from .v0043_kill_jobs_msg import V0043KillJobsMsg
from .v0043_kill_jobs_msg_flags_item import V0043KillJobsMsgFlagsItem
from .v0043_kill_jobs_msg_job_state_item import V0043KillJobsMsgJobStateItem
from .v0043_kill_jobs_resp_job import V0043KillJobsRespJob
from .v0043_kill_jobs_resp_job_error import V0043KillJobsRespJobError
from .v0043_kill_jobs_resp_job_federation import V0043KillJobsRespJobFederation
from .v0043_openapi_accounts_removed_resp import V0043OpenapiAccountsRemovedResp
from .v0043_openapi_accounts_resp import V0043OpenapiAccountsResp
from .v0043_openapi_assocs_removed_resp import V0043OpenapiAssocsRemovedResp
from .v0043_openapi_assocs_resp import V0043OpenapiAssocsResp
from .v0043_openapi_error import V0043OpenapiError
from .v0043_openapi_kill_jobs_resp import V0043OpenapiKillJobsResp
from .v0043_openapi_meta import V0043OpenapiMeta
from .v0043_openapi_meta_client import V0043OpenapiMetaClient
from .v0043_openapi_meta_plugin import V0043OpenapiMetaPlugin
from .v0043_openapi_meta_slurm import V0043OpenapiMetaSlurm
from .v0043_openapi_meta_slurm_version import V0043OpenapiMetaSlurmVersion
from .v0043_openapi_users_add_cond_resp import V0043OpenapiUsersAddCondResp
from .v0043_openapi_users_add_cond_resp_str import V0043OpenapiUsersAddCondRespStr
from .v0043_openapi_warning import V0043OpenapiWarning
from .v0043_tres import V0043Tres
from .v0043_uint_32_no_val_struct import V0043Uint32NoValStruct
from .v0043_user_short import V0043UserShort
from .v0043_user_short_adminlevel_item import V0043UserShortAdminlevelItem
from .v0043_users_add_cond import V0043UsersAddCond

__all__ = (
    "SlurmdbV0043PostUsersAssociationFlags",
    "V0043Account",
    "V0043AccountFlagsItem",
    "V0043Accounting",
    "V0043AccountingAllocated",
    "V0043Assoc",
    "V0043AssocDefault",
    "V0043AssocFlagsItem",
    "V0043AssocMax",
    "V0043AssocMaxJobs",
    "V0043AssocMaxJobsPer",
    "V0043AssocMaxPer",
    "V0043AssocMaxPerAccount",
    "V0043AssocMaxTres",
    "V0043AssocMaxTresGroup",
    "V0043AssocMaxTresMinutes",
    "V0043AssocMaxTresMinutesPer",
    "V0043AssocMaxTresPer",
    "V0043AssocMin",
    "V0043AssocRecSet",
    "V0043AssocShort",
    "V0043Coord",
    "V0043KillJobsMsg",
    "V0043KillJobsMsgFlagsItem",
    "V0043KillJobsMsgJobStateItem",
    "V0043KillJobsRespJob",
    "V0043KillJobsRespJobError",
    "V0043KillJobsRespJobFederation",
    "V0043OpenapiAccountsRemovedResp",
    "V0043OpenapiAccountsResp",
    "V0043OpenapiAssocsRemovedResp",
    "V0043OpenapiAssocsResp",
    "V0043OpenapiError",
    "V0043OpenapiKillJobsResp",
    "V0043OpenapiMeta",
    "V0043OpenapiMetaClient",
    "V0043OpenapiMetaPlugin",
    "V0043OpenapiMetaSlurm",
    "V0043OpenapiMetaSlurmVersion",
    "V0043OpenapiUsersAddCondResp",
    "V0043OpenapiUsersAddCondRespStr",
    "V0043OpenapiWarning",
    "V0043Tres",
    "V0043Uint32NoValStruct",
    "V0043UsersAddCond",
    "V0043UserShort",
    "V0043UserShortAdminlevelItem",
)
